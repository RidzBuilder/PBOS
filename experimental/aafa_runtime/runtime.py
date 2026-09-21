from dataclasses import dataclass, field
from typing import Any, Dict, List

@dataclass
class RuntimeState:
    status: str = "initialized"
    step: str = "observe"
    attempts: int = 0
    last_result: Any = None
    history: List[Dict[str, Any]] = field(default_factory=list)

@dataclass
class Memory:
    records: List[Dict[str, Any]] = field(default_factory=list)
    def add(self, record): self.records.append(record)

class CapabilityAdapter:
    capability = "transform_text"
    name = "base"
    def execute(self, payload): raise NotImplementedError

class UpperAdapter(CapabilityAdapter):
    name = "upper"
    def execute(self, payload): return {"text": payload["text"].upper()}

class LowerAdapter(CapabilityAdapter):
    name = "lower"
    def execute(self, payload): return {"text": payload["text"].lower()}

class FailingAdapter(CapabilityAdapter):
    name = "failing"
    def execute(self, payload): raise RuntimeError("simulated adapter failure")

class CapabilityRegistry:
    def __init__(self, adapters): self.adapters = {a.name:a for a in adapters}
    def resolve(self, capability, preferred=None, exclude=None):
        exclude=set(exclude or [])
        if preferred in self.adapters and preferred not in exclude and self.adapters[preferred].capability==capability: return self.adapters[preferred]
        for name,a in self.adapters.items():
            if name not in exclude and a.capability==capability: return a
        raise LookupError(f"no adapter for {capability}")

class Verifier:
    def verify(self, expected, observed): return expected == observed

class Evidence:
    def __init__(self): self.events=[]
    def record(self, kind, **data): self.events.append({"kind":kind, **data})

class Agent:
    def __init__(self, registry, verifier): self.registry=registry; self.verifier=verifier
    def run(self, goal, payload, expected, preferred=None):
        state=RuntimeState(); memory=Memory(); evidence=Evidence(); excluded=[]
        evidence.record("goal", goal=goal)
        for attempt in range(1,4):
            state.attempts=attempt; state.step="resolve"
            adapter=self.registry.resolve("transform_text", preferred=preferred, exclude=excluded)
            evidence.record("capability_resolved", capability="transform_text", adapter=adapter.name)
            state.step="act"
            try:
                result=adapter.execute(payload); state.last_result=result; state.step="verify"
                ok=self.verifier.verify(expected,result)
                evidence.record("action_result", adapter=adapter.name, result=result, verified=ok)
                memory.add({"adapter":adapter.name,"result":result,"verified":ok})
                if ok:
                    state.status="verified"; state.step="done"; evidence.record("final",status="verified",attempts=attempt); return state,memory,evidence
                excluded.append(adapter.name); evidence.record("recovery",reason="verification_failed",excluded=adapter.name)
            except Exception as exc:
                evidence.record("action_failure",adapter=adapter.name,error=str(exc)); excluded.append(adapter.name); state.step="recover"; evidence.record("recovery",reason="execution_failure",excluded=adapter.name)
        state.status="failed"; evidence.record("final",status="failed",attempts=state.attempts); return state,memory,evidence
