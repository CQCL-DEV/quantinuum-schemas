from quantinuum_schemas.models.backend_config import AerConfig


def test_instantiation() -> None:
    aer_config = AerConfig()
    assert isinstance(aer_config, AerConfig)
