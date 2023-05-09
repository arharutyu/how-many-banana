import pytest
from settingsoop import convert_from_m, Settings, Item


def test_convert_from_m():
    # test if item_length is zero
    assert convert_from_m(1,0) == '1.00'
    # test converted_length returns expected values
    assert convert_from_m(10,2) == '5.00'


testSettingsData = [
        {'item_name': 'banana', 'is_metric': False}
    ]

@pytest.fixture(scope="session", params=testSettingsData)
def update_settings(request):
        settings = Settings()
        settings.update_settings(request.param.get('item_name'), request.param.get('is_metric'))
        return settings
        # return settings.update_settings(request.param.get('item_name'), request.param.get('is_metric'))

def test_update_measure(update_settings):
        assert update_settings.item == 'banana'


testAddItem = [
       {'item_name':'grape', 'item_length': 'item_length'}
]

@pytest.fixture(scope="session", params=testAddItem)
def add_item(request):
       item = Item()
       item.add_item(request.params.get('item_name'), request.params.get('item_length'))
       return item



