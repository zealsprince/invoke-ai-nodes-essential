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

    a: float = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> BooleanOutput:
        return BooleanOutput(value=True if self.a != 0 else False)


@invocation("inttofloat", title="Integer to Float", tags=["cast", "math", "float", "integer"], category="cast")
class IntegerCastFloatInvocation(BaseInvocation):
    """Casts an integer to a float"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)

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
class FloatCeilInvocation(BaseInvocation):
    """Rounds a float and casts to an integer"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> IntegerOutput:
        return IntegerOutput(value=int(math.ceil(self.a)))


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

@invocation("floatsin", title="Float Sine (sin)", tags=["math", "float", "sine"], category="math")
class FloatSinInvocation(BaseInvocation):
    """Calculates the sine of a float as radians"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> FloatOutput:
        return FloatOutput(value=math.sin(self.a))
    

@invocation("floatcos", title="Float Cosine (cos)", tags=["math", "float", "cosine"], category="math")
class FloatCosInvocation(BaseInvocation):
    """Calculates the cosine of a float as radians"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> FloatOutput:
        return FloatOutput(value=math.cos(self.a))
    

@invocation("floattan", title="Float Tangent (tan)", tags=["math", "float", "tangent"], category="math")
class FloatTanInvocation(BaseInvocation):
    """Calculates the tangent of a float as radians"""

    a: float = InputField(default=0, description=FieldDescriptions.num_1)

    def invoke(self, context: InvocationContext) -> FloatOutput:
        return FloatOutput(value=math.tan(self.a))


@invocation("floatrand", title="Float Random", tags=["math", "float", "random"], category="math")
class FloatRandomInvocation(BaseInvocation):
    """Outputs a single random floating point number"""

    low: float = InputField(default=0, description="The inclusive low value")
    high: float = InputField(default=sys.float_info.max,
                             description="The exclusive high value")

    def invoke(self, context: InvocationContext) -> FloatOutput:
        return FloatOutput(value=float(random.uniform(self.low, self.high)))

# Float equals
# Float greaterthan
# Float lessthan
# Float greaterthanequals
# Float lessthanequals

# Float pow
# Float sqrt
# Float log

# Float asin
# Float acos
# Float atan
