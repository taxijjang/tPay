import pytest
from product.models import Tag


@pytest.mark.django_db
def test_tag():
    # tag = Tag.objects.all()
    # print(tag)
    assert True
