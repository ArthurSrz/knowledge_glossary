## Definition

Templates are a programming language feature that enables generic programming by allowing the creation of functions and classes that can operate with generic types, introduced in C++ by Bjarne Stroustrup in 1988 as part of his generic programming vision.

## Historical Development

1. **Early Vision (1981-1982)**: Stroustrup's initial concepts for parameterization
2. **Template Introduction (1988)**: First implementation in C++
3. **STL Integration (1994)**: Standard Template Library adoption
4. **Concept Proposals (2006)**: Attempt to formalize constraints
5. **C++20 Concepts**: Finally standardized constraints

## Stroustrup's Original Vision

According to Stroustrup's early papers:
- Type parameterization for code reuse
- Compile-time polymorphism
- Generic algorithms independent of data types
- Clean separation of algorithms and data structures
- Type safety without runtime overhead

## Key Features

1. **Function Templates**:
   - Generic function definitions
   - Type deduction
   - Overload resolution
   - Specialization support

2. **Class Templates**:
   - Generic class definitions
   - Member function templates
   - Static member support
   - Nested templates

3. **Template Parameters**:
   - Type parameters
   - Non-type parameters
   - Template template parameters
   - Variadic templates

## Core Mechanisms

1. **Template Instantiation**:
   - Compile-time expansion
   - Type substitution
   - Code generation
   - Specialization selection

2. **Template Argument Deduction**:
   - Automatic type inference
   - Deduction guides
   - SFINAE (Substitution Failure Is Not An Error)
   - Overload resolution

3. **Template Specialization**:
   - Full specialization
   - Partial specialization
   - Explicit instantiation
   - Member specialization

## Generic Programming Principles

1. **Type Independence**:
   - Algorithm/data structure separation
   - Interface-based design
   - Concept requirements
   - Duck typing

2. **Compile-time Polymorphism**:
   - Zero runtime overhead
   - Static type checking
   - Inlining opportunities
   - Optimization potential

3. **Code Reuse**:
   - Single implementation
   - Multiple type support
   - Library development
   - Framework creation

## Template Syntax

1. **Function Template**:
   ```cpp
   template<typename T>
   T max(T a, T b) {
       return (a > b) ? a : b;
   }
   ```

2. **Class Template**:
   ```cpp
   template<typename T>
   class Stack {
       std::vector<T> elements;
   public:
       void push(const T& element);
       T pop();
   };
   ```

## Advanced Features

1. **Template Metaprogramming**:
   - Compile-time computation
   - Type traits
   - SFINAE techniques
   - Constexpr functions

2. **Variadic Templates**:
   - Variable argument lists
   - Parameter packs
   - Pack expansion
   - Fold expressions

3. **Concepts (C++20)**:
   - Formal constraints
   - Requirement specification
   - Error message improvement
   - Interface contracts

## Applications

1. **Standard Template Library**:
   - Containers (vector, map)
   - Algorithms (sort, find)
   - Iterators
   - Function objects

2. **Modern C++ Libraries**:
   - Boost libraries
   - Eigen (linear algebra)
   - Qt templates
   - Game engines

3. **Other Languages**:
   - Java generics
   - C# generics
   - Rust generics
   - TypeScript generics

## Benefits

1. **Type Safety**:
   - Compile-time checking
   - No runtime casts
   - Strong typing
   - Error prevention

2. **Performance**:
   - Zero-cost abstraction
   - Inlining potential
   - Optimization opportunities
   - No virtual dispatch

3. **Maintainability**:
   - Single source of truth
   - Reduced code duplication
   - Clear interfaces
   - Modular design

## Challenges

1. **Compilation Complexity**:
   - Increased compile times
   - Code bloat potential
   - Complex error messages
   - Debugging difficulty

2. **Learning Curve**:
   - Syntax complexity
   - Conceptual difficulty
   - Advanced techniques
   - Best practices

## Scientific Impact

Stroustrup's templates:
- Revolutionized generic programming
- Influenced language design
- Enabled STL creation
- Shaped modern C++ development

## Related Concepts
- [[Generic programming]]
- [[Polymorphism]]
- [[Type systems]]
- [[Metaprogramming]]
- [[Standard Template Library]]

## References

Stroustrup, B. (1988). Parameterized Types for C++. Computing Systems, 2(1), 55-85.

Musser, D. R., & Stepanov, A. A. (1989). Generic programming. In International Symposium on Symbolic and Algebraic Computation (pp. 13-25). Springer.