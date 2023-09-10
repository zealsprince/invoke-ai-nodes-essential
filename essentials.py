# Copyright (c) 2023 Andrew Lake (https://github.com/zealsprince) zealsprince.com

from typing import Optional, Tuple

import sys
import random
import math
import numpy as np

from pydantic import BaseModel, Field

from .baseinvocation import BaseInvocation, FieldDescriptions, InputField, InvocationContext, invocation

from invokeai.app.invocations.primitives import BooleanOutput, IntegerOutput, FloatOutput

# 88888888ba                             88
# 88      "8b                            88
# 88      ,8P                            88
# 88aaaaaa8P'   ,adPPYba,    ,adPPYba,   88   ,adPPYba,  ,adPPYYba,  8b,dPPYba,
# 88""""""8b,  a8"     "8a  a8"     "8a  88  a8P_____88  ""     `Y8  88P'   `"8a
# 88      `8b  8b       d8  8b       d8  88  8PP"""""""  ,adPPPPP88  88       88
# 88      a8P  "8a,   ,a8"  "8a,   ,a8"  88  "8b,   ,aa  88,    ,88  88       88
# 88888888P"    `"YbbdP"'    `"YbbdP"'   88   `"Ybbd8"'  `"8bbdP"Y8  88       88


@invocation("booltoint", title="Boolean to Integer", tags=["cast", "math", "boolean", "integer"], category="cast")
class BooleanCastInteger(BaseInvocation):
    """Casts a boolean to an integer"""

    a: bool = InputField(default=True, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> BooleanOutput:
        return IntegerOutput(value=1 if self.a == True else 0)


@invocation("booltofloat", title="Boolean to Float", tags=["cast", "math", "boolean", "float"], category="cast")
class BooleanCastFloat(BaseInvocation):
    """Casts a boolean to a float"""

    a: bool = InputField(default=True, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> BooleanOutput:
        return FloatOutput(value=1.0 if self.a == True else 0)


@invocation("boolnot", title="Boolean Not (!)", tags=["logic", "math", "boolean", "not"], category="logic")
class BooleanNotInvocation(BaseInvocation):
    """Inverses a boolean"""

    a: bool = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> BooleanOutput:
        return BooleanOutput(value=not self.value)


@invocation("boolequals", title="Boolean Equals (==)", tags=["logic", "condition", "boolean", "equal"], category="logic")
class BooleanEqualsInvocation(BaseInvocation):
    """Compares two booleans"""

    a: bool = InputField(default=True, description=FieldDescriptions.num_1)
    b: bool = InputField(default=True, description=FieldDescriptions.num_2)

    def invoke(self, context: InvocationContext) -> BooleanOutput:
        return BooleanOutput(value=self.a == self.b)


@invocation("boolrand", title="Boolean Random", tags=["math", "boolean", "random"], category="math")
class BooleanRandomInvocation(BaseInvocation):
    """Outputs a random boolean"""

    def invoke(self, context: InvocationContext) -> BooleanOutput:
        return BooleanOutput(value=np.random.randint(0, 2) == 0)

# 88
# 88                ,d
# 88                88
# 88  8b,dPPYba,  MM88MMM  ,adPPYba,   ,adPPYb,d8   ,adPPYba,  8b,dPPYba,
# 88  88P'   `"8a   88    a8P_____88  a8"    `Y88  a8P_____88  88P'   "Y8
# 88  88       88   88    8PP"""""""  8b       88  8PP"""""""  88
# 88  88       88   88,   "8b,   ,aa  "8a,   ,d88  "8b,   ,aa  88
# 88  88       88   "Y888  `"Ybbd8"'   `"YbbdP"Y8   `"Ybbd8"'  88
#                                      aa,    ,88
#                                       "Y8bbdP"


@invocation("inttobool", title="Integer to Boolean", tags=["cast", "math", "float", "boolean"], category="cast")
class IntegerCastBooleanInvocation(BaseInvocation):
    """Casts an integer to a boolean"""

    a: int = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> BooleanOutput:
        return BooleanOutput(value=True if self.a != 0 else False)


@invocation("inttofloat", title="Integer to Float", tags=["cast", "math", "float", "integer"], category="cast")
class IntegerCastFloatInvocation(BaseInvocation):
    """Casts an integer to a float"""

    a: int = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> FloatOutput:
        return FloatOutput(value=int(self.a))


@invocation("intadd", title="Integer Addition (+)", tags=["math", "integer", "add"], category="math")
class IntegerAddInvocation(BaseInvocation):
    """Adds two integers"""

    a: int = InputField(default=0, description=FieldDescriptions.num_1)
    b: int = InputField(default=0, description=FieldDescriptions.num_2)

    def invoke(self, context: InvocationContext) -> IntegerOutput:
        return IntegerOutput(value=self.a + self.b)


@invocation("intsub", title="Integer Subtraction (-)", tags=["math", "integer", "subtract"], category="math")
class IntegerSubtractInvocation(BaseInvocation):
    """Subtracts two integers"""

    a: int = InputField(default=0, description=FieldDescriptions.num_1)
    b: int = InputField(default=0, description=FieldDescriptions.num_2)

    def invoke(self, context: InvocationContext) -> IntegerOutput:
        return IntegerOutput(value=self.a - self.b)


@invocation("intmul", title="Integer Multiplication (*)", tags=["math", "integer",  "multiply"], category="math")
class IntegerMultiplyInvocation(BaseInvocation):
    """Multiplies two integers"""

    a: int = InputField(default=0, description=FieldDescriptions.num_1)
    b: int = InputField(default=0, description=FieldDescriptions.num_2)

    def invoke(self, context: InvocationContext) -> IntegerOutput:
        return IntegerOutput(value=self.a * self.b)


@invocation("intdiv", title="Integer Division (/)", tags=["math", "integer", "divide"], category="math")
class IntegerDivideInvocation(BaseInvocation):
    """Divides two integers"""

    a: int = InputField(default=0, description=FieldDescriptions.num_1)
    b: int = InputField(default=0, description=FieldDescriptions.num_2)

    def invoke(self, context: InvocationContext) -> IntegerOutput:
        return IntegerOutput(value=int(self.a / self.b))


@invocation("intmodulo", title="Integer Modulo (%)", tags=["math", "integer", "modulo"], category="math")
class IntegerModuloInvocation(BaseInvocation):
    """Calculates the remainder of a division as an integer"""

    a: int = InputField(default=0, description=FieldDescriptions.num_1)
    b: int = InputField(default=0, description=FieldDescriptions.num_2)

    def invoke(self, context: InvocationContext) -> IntegerOutput:
        return IntegerOutput(value=self.a % self.b)


@invocation("intabs", title="Integer Absolute (abs)", tags=["math", "integer", "absolute"], category="math")
class IntegerAbsoluteInvocation(BaseInvocation):
    """Calculates the absolute value of an integer"""

    a: int = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> IntegerOutput:
        return IntegerOutput(value=math.abs(self.a))


@invocation("intrand", title="Integer Random", tags=["math", "integer", "random"], category="math")
class IntegerRandomInvocation(BaseInvocation):
    """Outputs a single random integer"""

    low: int = InputField(default=0, description="The inclusive low value")
    high: int = InputField(default=np.iinfo(np.int32).max,
                           description="The exclusive high value")

    def invoke(self, context: InvocationContext) -> IntegerOutput:
        return IntegerOutput(value=np.random.randint(self.low, self.high))


@invocation("intequals", title="Integer Equals (==)", tags=["logic", "condition", "int", "equal"], category="logic")
class IntegerEqualsInvocation(BaseInvocation):
    """Compares two Integers"""

    a: int = InputField(default=True, description=FieldDescriptions.num_1)
    b: int = InputField(default=True, description=FieldDescriptions.num_2)

    def invoke(self, context: InvocationContext) -> BooleanOutput:
        return BooleanOutput(value=self.a == self.b)


@invocation("intgreater", title="Integer Greater Than (>)", tags=["logic", "condition", "int", "greater"], category="logic")
class IntegerGreaterInvocation(BaseInvocation):
    """Compares if one Integer is greater than another"""

    a: int = InputField(default=True, description=FieldDescriptions.num_1)
    b: int = InputField(default=True, description=FieldDescriptions.num_2)

    def invoke(self, context: InvocationContext) -> BooleanOutput:
        return BooleanOutput(value=self.a > self.b)


@invocation("intgreaterequals", title="Integer Greater or Equal Than (>=)", tags=["logic", "condition", "int", "greater", "equal"], category="logic")
class IntegerGreaterEqualsInvocation(BaseInvocation):
    """Compares if one Integer is greater than or equal to another"""

    a: int = InputField(default=True, description=FieldDescriptions.num_1)
    b: int = InputField(default=True, description=FieldDescriptions.num_2)

    def invoke(self, context: InvocationContext) -> BooleanOutput:
        return BooleanOutput(value=self.a >= self.b)


@invocation("intless", title="Integer Less Than (<)", tags=["logic", "condition", "int", "less"], category="logic")
class IntegerLessInvocation(BaseInvocation):
    """Compares if one Integer is less than another"""

    a: int = InputField(default=True, description=FieldDescriptions.num_1)
    b: int = InputField(default=True, description=FieldDescriptions.num_2)

    def invoke(self, context: InvocationContext) -> BooleanOutput:
        return BooleanOutput(value=self.a < self.b)


@invocation("intlessequals", title="Integer Less or Equal Than (<=)", tags=["logic", "condition", "int", "less", "equal"], category="logic")
class IntegerLessEqualsInvocation(BaseInvocation):
    """Compares if one Integer is less than or equal to another"""

    a: int = InputField(default=True, description=FieldDescriptions.num_1)
    b: int = InputField(default=True, description=FieldDescriptions.num_2)

    def invoke(self, context: InvocationContext) -> BooleanOutput:
        return BooleanOutput(value=self.a <= self.b)

# 88888888888  88
# 88           88                             ,d
# 88           88                             88
# 88aaaaa      88   ,adPPYba,   ,adPPYYba,  MM88MMM
# 88"""""      88  a8"     "8a  ""     `Y8    88
# 88           88  8b       d8  ,adPPPPP88    88
# 88           88  "8a,   ,a8"  88,    ,88    88,
# 88           88   `"YbbdP"'   `"8bbdP"Y8    "Y888


@invocation("floattobool", title="Float to Boolean", tags=["cast", "math", "float", "boolean"], category="cast")
class FloatCastBooleanInvocation(BaseInvocation):
    """Casts a float to a boolean"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> BooleanOutput:
        return BooleanOutput(value=True if self.a != 0 else False)


@invocation("floattoint", title="Float to Integer", tags=["cast", "math", "float", "integer"], category="cast")
class FloatCastIntegerInvocation(BaseInvocation):
    """Casts a float to an integer"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> IntegerOutput:
        return IntegerOutput(value=int(self.a))


@invocation("floatadd", title="Float Addition (+)", tags=["math", "float", "add"], category="math")
class FloatAddInvocation(BaseInvocation):
    """Adds two floating point numbers"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)
    b: float = InputField(default=0, description=FieldDescriptions.num_2)

    def invoke(self, context: InvocationContext) -> FloatOutput:
        return FloatOutput(value=self.a + self.b)


@invocation("floatsub", title="Float Subtraction (-)", tags=["math", "float", "subtract"], category="math")
class FloatSubtractInvocation(BaseInvocation):
    """Subtracts two floating point numbers"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)
    b: float = InputField(default=0, description=FieldDescriptions.num_2)

    def invoke(self, context: InvocationContext) -> FloatOutput:
        return FloatOutput(value=self.a - self.b)


@invocation("floatmul", title="Float Multiplication (*)", tags=["math", "float",  "multiply"], category="math")
class FloatMultiplyInvocation(BaseInvocation):
    """Multiplies two floating point numbers"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)
    b: float = InputField(default=0, description=FieldDescriptions.num_2)

    def invoke(self, context: InvocationContext) -> FloatOutput:
        return FloatOutput(value=self.a * self.b)


@invocation("floatdiv", title="Float Division (/)", tags=["math", "float", "divide"], category="math")
class FloatDivideInvocation(BaseInvocation):
    """Divides two floating point numbers"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)
    b: float = InputField(default=0, description=FieldDescriptions.num_2)

    def invoke(self, context: InvocationContext) -> FloatOutput:
        return FloatOutput(value=self.a / self.b)


@invocation("floatmodulo", title="Float Modulo (%)", tags=["math", "float", "modulo"], category="math")
class FloatModuloInvocation(BaseInvocation):
    """Calculates the remainder of a division as a float"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)
    b: float = InputField(default=0, description=FieldDescriptions.num_2)

    def invoke(self, context: InvocationContext) -> FloatOutput:
        return FloatOutput(value=self.a % self.b)


@invocation("floatabs", title="Float Absolute (abs)", tags=["math", "float", "absolute"], category="math")
class FloatAbsoluteInvocation(BaseInvocation):
    """Calculates the absolute value of a float"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> FloatOutput:
        return FloatOutput(value=math.abs(self.a))
    

@invocation("floatround", title="Float Round (round)", tags=["math", "float", "integer", "round"], category="math")
class FloatRoundInvocation(BaseInvocation):
    """Rounds a float and casts to an integer"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> IntegerOutput:
        return IntegerOutput(value=int(math.round(self.a)))


@invocation("floatroundtomultiple", title="Float Round To Multiple", tags=["math", "float", "integer", "round"], category="math")
class FloatRoundToMultipleInvocation(BaseInvocation):
    """Rounds a float to the next multiple of N and casts to an integer"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)
    n: float = InputField(default=8, description=FieldDescriptions.num_2)

    def invoke(self, context: InvocationContext) -> IntegerOutput:
        return IntegerOutput(value=int(self.a // self.n * self.n))

@invocation("floatceil", title="Float Ceiling (ceil)", tags=["math", "float", "integer", "ceiling"], category="math")
class FloatCeilInvocation(BaseInvocation):
    """Rounds a float up and casts to an integer"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> IntegerOutput:
        return IntegerOutput(value=int(math.ceil(self.a)))
    

@invocation("floatfloor", title="Float Floor (floor)", tags=["math", "float", "integer", "floor"], category="math")
class FloatFloorInvocation(BaseInvocation):
    """Rounds a float down and casts to an integer"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> IntegerOutput:
        return IntegerOutput(value=int(math.floor(self.a)))


@invocation("floatpow", title="Float Raise Power (pow)", tags=["math", "float", "pow"], category="math")
class FloatPowInvocation(BaseInvocation):
    """Raises a float to the power of a value"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)
    b: int = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> FloatOutput:
        return FloatOutput(value=math.pow(self.a, self.b))


@invocation("floatsqrt", title="Float Square Root (sqrt)", tags=["math", "float", "sqrt"], category="math")
class FloatSqrtInvocation(BaseInvocation):
    """Calculates the square root of a float"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> FloatOutput:
        return FloatOutput(value=math.sqrt(self.a))


@invocation("floatlog", title="Float Logarithm (log)", tags=["math", "float", "log"], category="math")
class FloatLogInvocation(BaseInvocation):
    """Calculates the natural logarithm of a float"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> FloatOutput:
        return FloatOutput(value=math.log(self.a))
    
@invocation("floatlogn", title="Float Logarithm N (logn)", tags=["math", "float", "log"], category="math")
class FloatLogNInvocation(BaseInvocation):
    """Calculates the logarithm of a float to a base N"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)
    n: int = InputField(default=0, description=FieldDescriptions.num_2)

    def invoke(self, context: InvocationContext) -> FloatOutput:
        return FloatOutput(value=math.log(self.a, self.n))

@invocation("floatsin", title="Float Sine (sin)", tags=["math", "float", "sine"], category="math")
class FloatSineInvocation(BaseInvocation):
    """Calculates the sine of a float as radians"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> FloatOutput:
        return FloatOutput(value=math.sin(self.a))
    

@invocation("floatcos", title="Float Cosine (cos)", tags=["math", "float", "cosine"], category="math")
class FloatCosineInvocation(BaseInvocation):
    """Calculates the cosine of a float as radians"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> FloatOutput:
        return FloatOutput(value=math.cos(self.a))

@invocation("floattan", title="Float Tangent (tan)", tags=["math", "float", "tangent"], category="math")
class FloatTangentInvocation(BaseInvocation):
    """Calculates the tangent of a float as radians"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> FloatOutput:
        return FloatOutput(value=math.tan(self.a))


@invocation("floatsinh", title="Float Hyperbolic Tangent (sinh)", tags=["math", "float", "sine", "hyerbolic"], category="math")
class FloatHyperbolicSineInvocation(BaseInvocation):
    """Calculates the hyperbolic sine of a float as radians"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> FloatOutput:
        return FloatOutput(value=math.sinh(self.a))


@invocation("floatcosh", title="Float Hyperbolic Cosine (cosh)", tags=["math", "float", "cosine", "hyerbolic"], category="math")
class FloatHyperbolicCosineInvocation(BaseInvocation):
    """Calculates the hyperbolic cosine of a float as radians"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> FloatOutput:
        return FloatOutput(value=math.cosh(self.a))


@invocation("floattanh", title="Float Hyperbolic Tangent (tanh)", tags=["math", "float", "tangent", "hyerbolic"], category="math")
class FloatHyperbolicTangentInvocation(BaseInvocation):
    """Calculates the hyperbolic tangent of a float as radians"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> FloatOutput:
        return FloatOutput(value=math.tanh(self.a))

@invocation("floatasin", title="Float Arc Tangent (asin)", tags=["math", "float", "sine", "arc"], category="math")
class FloatArcSineInvocation(BaseInvocation):
    """Calculates the arc sine of a float as radians"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> FloatOutput:
        return FloatOutput(value=math.asin(self.a))
    
@invocation("floatacos", title="Float Arc Cosine (acos)", tags=["math", "float", "cosine", "arc"], category="math")
class FloatArcCosineInvocation(BaseInvocation):
    """Calculates the arc cosine of a float as radians"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> FloatOutput:
        return FloatOutput(value=math.acos(self.a))

@invocation("floatatan", title="Float Arc Tangent (atan)", tags=["math", "float", "tangent", "arc"], category="math")
class FloatArcTangentInvocation(BaseInvocation):
    """Calculates the arc tangent of a float as radians"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> FloatOutput:
        return FloatOutput(value=math.atan(self.a))


@invocation("floatasinh", title="Float Inverse Hyperbolic Tangent (asinh)", tags=["math", "float", "sine", "hyerbolic"], category="math")
class FloatInverseHyerbolicSineInvocation(BaseInvocation):
    """Calculates the inverse hyperbolic sine of a float as radians"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> FloatOutput:
        return FloatOutput(value=math.asinh(self.a))


@invocation("floatacosh", title="Float Inverse Hyperbolic Cosine (acosh)", tags=["math", "float", "cosine", "hyerbolic"], category="math")
class FloatInverseHyerbolicCosineInvocation(BaseInvocation):
    """Calculates the inverse hyperbolic cosine of a float as radians"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> FloatOutput:
        return FloatOutput(value=math.acosh(self.a))


@invocation("floatatanh", title="Float Inverse Hyperbolic Tangent (atanh)", tags=["math", "float", "tangent", "hyerbolic"], category="math")
class FloatInverseHyerbolicTangentInvocation(BaseInvocation):
    """Calculates the inverse hyperbolic tangent of a float as radians"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> FloatOutput:
        return FloatOutput(value=math.atanh(self.a))

@invocation("floatrand", title="Float Random", tags=["math", "float", "random"], category="math")
class FloatRandomInvocation(BaseInvocation):
    """Outputs a single random floating point number"""

    low: float = InputField(default=0, description="The inclusive low value")
    high: float = InputField(default=sys.float_info.max,
                             description="The exclusive high value")

    def invoke(self, context: InvocationContext) -> FloatOutput:
        return FloatOutput(value=float(random.uniform(self.low, self.high)))


@invocation("floatequals", title="Float Equals (==)", tags=["logic", "condition", "float", "equal", "boolean"], category="logic")
class FloatEqualsInvocation(BaseInvocation):
    """Compares two floating point numbers"""

    a: float = InputField(default=True, description=FieldDescriptions.num_1)
    b: float = InputField(default=True, description=FieldDescriptions.num_2)

    def invoke(self, context: InvocationContext) -> BooleanOutput:
        return BooleanOutput(value=self.a == self.b)
    

@invocation("floatgreater", title="Float Greater Than (>)", tags=["logic", "condition", "float", "greater", "boolean"], category="logic")
class FloatGreaterInvocation(BaseInvocation):
    """Compares if one floating point number is greater than another"""

    a: float = InputField(default=True, description=FieldDescriptions.num_1)
    b: float = InputField(default=True, description=FieldDescriptions.num_2)

    def invoke(self, context: InvocationContext) -> BooleanOutput:
        return BooleanOutput(value=self.a > self.b)


@invocation("floatgreaterequals", title="Float Greater or Equal Than (>=)", tags=["logic", "condition", "float", "greater", "equal", "boolean"], category="logic")
class FloatGreaterEqualsInvocation(BaseInvocation):
    """Compares if one floating point number is greater than or equal to another"""

    a: float = InputField(default=True, description=FieldDescriptions.num_1)
    b: float = InputField(default=True, description=FieldDescriptions.num_2)

    def invoke(self, context: InvocationContext) -> BooleanOutput:
        return BooleanOutput(value=self.a >= self.b)


@invocation("floatless", title="Float Less Than (<)", tags=["logic", "condition", "float", "less", "boolean"], category="logic")
class FloatLessInvocation(BaseInvocation):
    """Compares if one floating point number is less than another"""

    a: float = InputField(default=True, description=FieldDescriptions.num_1)
    b: float = InputField(default=True, description=FieldDescriptions.num_2)

    def invoke(self, context: InvocationContext) -> BooleanOutput:
        return BooleanOutput(value=self.a < self.b)


@invocation("floatlessequals", title="Float Less or Equal Than (<=)", tags=["logic", "condition", "float", "less", "equal", "boolean"], category="logic")
class FloatLessEqualsInvocation(BaseInvocation):
    """Compares if one floating point number is less than or equal to another"""

    a: float = InputField(default=True, description=FieldDescriptions.num_1)
    b: float = InputField(default=True, description=FieldDescriptions.num_2)

    def invoke(self, context: InvocationContext) -> BooleanOutput:
        return BooleanOutput(value=self.a <= self.b)