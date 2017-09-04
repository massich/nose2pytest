from tests.test_script import check_passes
from nose2pytest.script import NoseConversionRefactoringTool

if __name__ == "__main__":
    refac = NoseConversionRefactoringTool()
    check_passes(refac, 'assert_almost_equal(123.456, 123.5, delta=0.1)',
                    'assert 123.456 - 123.5 <= 0.1')
