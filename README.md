# Invoke AI Node Essentials

Extension for [InvokeAI](https://github.com/invoke-ai/InvokeAI "InvokeAI")'s node editor containing essential math and logic functions.

This collection of nodes was created out of a desire to build more dynamic and conditional workflows and aims to close what to me felt like a gap in the built-in functions and nodes that ship with InvokeAI.

I plan on expanding these nodes with more essential workflow modules such as basic image editing to close a gap in functionality there as well.

## Installation

To install, place the `.py` files into your InvokeAI invocations folder located here:

Windows - `invokeai\.venv\Lib\site-packages\invokeai\app\invocations\`
<br>Mac/Linux - `invokeai/.venv/lib/python3.10/site-packages/invokeai/app/invocations/`

## Example Use

![Example](https://user-images.githubusercontent.com/1859270/266791992-ad47eca8-aed3-4f62-81bc-ef5cd5354188.png)

## Functions

|Function|Title|Description|
|---|---|---|
| BooleanCastInteger | Boolean to Integer | Casts a boolean to an integer
| BooleanCastFloat | Boolean to Float | Casts a boolean to a float
| BooleanNotInvocation | Boolean Not (!) | Inverses a boolean
| BooleanEqualsInvocation | Boolean Equals (==) | Compares two booleans
| BooleanRandomInvocation | Boolean Random | Outputs a random boolean
| IntegerCastBooleanInvocation | Integer to Boolean | Casts an integer to a boolean
| IntegerCastFloatInvocation | Integer to Float | Casts an integer to a float
| IntegerAddInvocation | Integer Addition (+) | Adds two integers
| IntegerSubtractInvocation | Integer Subtraction (-) | Subtracts two integers
| IntegerMultiplyInvocation | Integer Multiplication (*) | Multiplies two integers
| IntegerDivideInvocation | Integer Division (/) | Divides two integers
| IntegerModuloInvocation | Integer Modulo (%) | Calculates the remainder of a division as an integer
| IntegerAbsoluteInvocation | Integer Absolute (abs) | Calculates the absolute value of an integer
| IntegerRandomInvocation | Integer Random | Outputs a single random integer
| IntegerEqualsInvocation | Integer Equals (==) | Compares two Integers
| IntegerGreaterInvocation | Integer Greater Than (>) | Compares if one Integer is greater than another
| IntegerGreaterEqualsInvocation | Integer Greater or Equal Than (>=) | Compares if one Integer is greater than or equal to another
| IntegerLessInvocation | Integer Less Than (<) | Compares if one Integer is less than another
| IntegerLessEqualsInvocation | Integer Less or Equal Than (<=) | Compares if one Integer is less than or equal to another
| FloatCastBooleanInvocation | Float to Boolean | Casts a float to a boolean
| FloatCastIntegerInvocation | Float to Integer | Casts a float to an integer
| FloatAddInvocation | Float Addition (+) | Adds two floating point numbers
| FloatSubtractInvocation | Float Subtraction (-) | Subtracts two floating point numbers
| FloatMultiplyInvocation | Float Multiplication (*) | Multiplies two floating point numbers
| FloatDivideInvocation | Float Division (/) | Divides two floating point numbers
| FloatModuloInvocation | Float Modulo (%) | Calculates the remainder of a division as a float
| FloatAbsoluteInvocation | Float Absolute (abs) | Calculates the absolute value of a float
| FloatCeilInvocation | Float Round (round) | Rounds a float and casts to an integer
| FloatCeilInvocation | Float Ceiling (ceil) | Rounds a float up and casts to an integer
| FloatFloorInvocation | Float Floor (floor) | Rounds a float down and casts to an integer
| FloatPowInvocation | Float Raise Power (pow) | Raises a float to the power of a value
| FloatSqrtInvocation | Float Square Root (sqrt) | Calculates the square root of a float
| FloatLogInvocation | Float Logarithm (log) | Calculates the natural logarithm of a float
| FloatLogNInvocation | Float Logarithm N (logn) | Calculates the logarithm of a float to a base N
| FloatSineInvocation | Float Sine (sin) | Calculates the sine of a float as radians
| FloatCosineInvocation | Float Cosine (cos) | Calculates the cosine of a float as radians
| FloatTangentInvocation | Float Tangent (tan) | Calculates the tangent of a float as radians
| FloatHyperbolicSineInvocation | Float Hyperbolic Tangent (sinh) | Calculates the hyperbolic sine of a float as radians
| FloatHyperbolicCosineInvocation | Float Hyperbolic Cosine (cosh) | Calculates the hyperbolic cosine of a float as radians
| FloatHyperbolicTangentInvocation | Float Hyperbolic Tangent (tanh) | Calculates the hyperbolic tangent of a float as radians
| FloatArcSineInvocation | Float Arc Tangent (asin) | Calculates the arc sine of a float as radians
| FloatArcCosineInvocation | Float Arc Cosine (acos) | Calculates the arc cosine of a float as radians
| FloatArcTangentInvocation | Float Arc Tangent (atan) | Calculates the arc tangent of a float as radians
| FloatInverseHyerbolicSineInvocation | Float Inverse Hyperbolic Tangent (asinh) | Calculates the inverse hyperbolic sine of a float as radians
| FloatInverseHyerbolicCosineInvocation | Float Inverse Hyperbolic Cosine (acosh) | Calculates the inverse hyperbolic cosine of a float as radians
| FloatInverseHyerbolicTangentInvocation | Float Inverse Hyperbolic Tangent (atanh) | Calculates the inverse hyperbolic tangent of a float as radians
| FloatRandomInvocation | Float Random | Outputs a single random floating point number
| FloatEqualsInvocation | Float Equals (==) | Compares two floating point numbers
| FloatGreaterInvocation | Float Greater Than (>) | Compares if one floating point number is greater than another
| FloatGreaterEqualsInvocation | Float Greater or Equal Than (>=) | Compares if one floating point number is greater than or equal to another
| FloatLessInvocation | Float Less Than (<) | Compares if one floating point number is less than another
| FloatLessEqualsInvocation | Float Less or Equal Than (<=) | Compares if one floating point number is less than or equal to another
