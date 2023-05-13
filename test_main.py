import pytest
from settingsoop import convert_from_m, convert_from_i, Settings, Item


##CONVERT FEATURE TESTS##
def test_convert_from_m():
    # test if item_length is zero
    assert convert_from_m(1,0) == '1.00'
    # test converted_length returns expected values
    assert convert_from_m(10,2) == '5.00'

def test_convert_from_i():
       #test expected values
       assert convert_from_i(0,10) == .254
       #test invalid arg 
       assert convert_from_i('a', 2) == 1
       
##UPDATE SETTINGS TESTS (is_metric)##
testSettingsData = [
        {'item_name': 'banana', 'is_metric': False}
    ]

@pytest.fixture(scope="session", params=testSettingsData)
def update_settings(request):
        settings = Settings()
        settings.update_settings(request.param.get('item_name'), request.param.get('is_metric'))
        return settings


def test_update_settings(update_settings):
        # test is_metric attribute of Settings has updated
        assert update_settings.is_metric == 'False'
        # test item attribute of Settings
        assert update_settings.item == 'banana'

##UPDATE SETTINGS TESTS (item)##
testItemData = [
       {'item_name':'grape', 'item_length': '0.01'}
]

@pytest.fixture(scope="session", params=testItemData)
def add_item(request):
       item = Item(request.param.get('item_name'))
       item.add_item(request.param.get('item_name'), request.param.get('item_length'))
       return item

def test_add_item(add_item):
       #test item name attribute of Item has added
       assert add_item.item_name == 'grape'
       #test item length attribute of Item has added
       assert add_item.item_length == '0.01'
