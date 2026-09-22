from runtime import *


def test_happy_path_and_adapter_swap():
    reg = CapabilityRegistry([UpperAdapter(), LowerAdapter()]); agent = Agent(reg, Verifier())
    s, m, e = agent.run("uppercase", {"text": "Ridz"}, {"text": "RIDZ"}, preferred="upper")
    assert s.status == "verified" and s.attempts == 1
    s, m, e = agent.run("lowercase", {"text": "RIDZ"}, {"text": "ridz"}, preferred="lower")
    assert s.status == "verified" and any(x["adapter"] == "lower" for x in m.records)


def test_recovery_after_failure():
    reg = CapabilityRegistry([FailingAdapter(), UpperAdapter()]); agent = Agent(reg, Verifier())
    s, m, e = agent.run("recover", {"text": "Ridz"}, {"text": "RIDZ"}, preferred="failing")
    assert s.status == "verified" and s.attempts == 2
    kinds = [x["kind"] for x in e.events]
    assert "action_failure" in kinds and "recovery" in kinds


def test_verification_failure_recovers():
    reg = CapabilityRegistry([LowerAdapter(), UpperAdapter()]); agent = Agent(reg, Verifier())
    s, m, e = agent.run("verify-recover", {"text": "Ridz"}, {"text": "RIDZ"}, preferred="lower")
    assert s.status == "verified" and s.attempts == 2


def test_real_local_environment_execution():
    from pathlib import Path
    p = Path("/tmp/pbos_environment_artifact.txt")
    reg = CapabilityRegistry([FileUpperAdapter()]); agent = Agent(reg, Verifier())
    expected = {"path": str(p), "text": "RIDZ"}
    s, m, e = agent.run("write artifact", {"path": str(p), "text": "Ridz"}, expected, preferred="file_upper")
    assert s.status == "verified" and p.read_text() == "RIDZ"


if __name__ == "__main__":
    test_happy_path_and_adapter_swap()
    test_recovery_after_failure()
    test_verification_failure_recovers()
    test_real_local_environment_execution()
    print("PBOS_RUNTIME_CONFORMANCE=PASS")
