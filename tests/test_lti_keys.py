import gofer_service.lti_keys as lti
import pytest
import os


@pytest.fixture
def setup():
    os.environ["GCP_PROJECT_ID"] =  "data8x-scratch"
    os.environ["LTI_CONSUMER_KEY"] =  "TEST_ENV_KEY"
    yield
    if 'GCP_PROJECT_ID' in os.environ:
        del os.environ['GCP_PROJECT_ID']
    if 'LTI_CONSUMER_KEY' in os.environ:
        del os.environ['LTI_CONSUMER_KEY']


def test_get_secrets(setup):
    key = lti.get_via_gcp_secrets("LTI_CONSUMER_KEY")
    assert "b34eeb75dca9b467b1e074" in key


def test_get_via_env(setup):
    key = lti.get_via_env("LTI_CONSUMER_KEY")
    assert "TEST_ENV_KEY" in key


def test_get(setup):
    key = lti.get("LTI_CONSUMER_KEY")
    assert "b34eeb75dca9b467b1e074" in key
    del os.environ['GCP_PROJECT_ID']
    key = lti.get("LTI_CONSUMER_KEY")
    assert "TEST_ENV_KEY" in key
    del os.environ['LTI_CONSUMER_KEY']
    try:
        key = lti.get("LTI_CONSUMER_KEY") # this should raise Exception
        assert False
    except Exception:
        assert True