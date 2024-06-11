#Project Name: integration_test
#Developer: Reshma
#Description: This task will create integration test cases to test all possible negative and positive scenarios

import pythagorean_theorem
import calculator

# Pass the right and left side angle values of triangle for the positive test case
def test_sides():
    assert pythagorean_theorem.trianglesides(6,8) == 100
    print("Its runnig")

# Pass the triangle sides calculated value for the negative test case
def test_hypotenuse():
    assert pythagorean_theorem.hypotenuse(100) == 100