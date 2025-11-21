# mypy: disable-error-code=no-untyped-def

from rss_read_and_feed.enums.parser import MediaType


def test_values_are_tuple_of_str():
    for mt in MediaType:
        assert isinstance(mt.value, tuple)
        assert all(isinstance(x, str) for x in mt.value)


def test_json_factory_contains_expected_mimes():
    expected = {"application/json"}
    assert expected.issubset(set(MediaType.JSON.value))


def test_xml_factory_contains_expected_mimes() -> None:
    expected = {"application/xml", "text/xml"}
    assert expected.issubset(set(MediaType.XML.value))


def test_members_have_no_overlap():
    values = {m: set(m.value) for m in MediaType}
    members = list(values.keys())
    for i in range(len(members)):
        for j in range(i + 1, len(members)):
            assert values[members[i]].isdisjoint(
                values[members[j]]
            ), f"Overlap between {members[i].name} and {members[j].name}"
