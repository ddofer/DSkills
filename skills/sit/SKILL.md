---
name: sit
description: Systematic Inventive Thinking for new ideas and stuck problems. Changes the structure of the existing system first, then asks what the change is good for. Manual only; start with /sit <goal, problem or trade-off>.
disable-model-invocation: true
argument-hint: "<what to invent, or the obstacle or trade-off to get past>"
---

Task: $ARGUMENTS

## Steps

1. **Lay out the system.** The goal, or the obstacle and what must stay fixed. Then the parts: components, what each does, their variable properties, and what sits next to the system (data, people, steps, hardware, the environment). For an obstacle, separate real limits (physics, compute, money) from habits and untested assumptions.
2. **Change the shape, inside the closed world.** Use only what is already there. Apply the operators that fit; not all five:
   - **Subtract** an essential part, and at first its function too, without replacing it. Removing an unwanted part is not the operator.
   - **Multiply** a part, with the copy changed in some way.
   - **Divide** a part or a step and put the pieces somewhere else, or in a different order.
   - **Unify tasks:** an existing part takes on another job.
   - **Change a dependency:** make a property vary with something it did not before, or stop it varying.

   For an obstacle, name the harmful factor and the effect it causes, then look for a shape in which the effect no longer depends on that factor, or the factor does useful work instead. For a trade-off, state it as one parameter that needs two opposite values, then ask when, where, under which condition or at which level each value is needed, and separate them there.
3. **Ask what each new shape is good for.** Only now judge: what does it make possible, by what mechanism, under what conditions, what new limit does it bring. Drop the ones with no mechanism.
4. **Go outside the closed world** only if the inside gave little: an assumption to drop, or a mechanism borrowed from another field.
5. **Report** the distinct ideas, the ones that differ by mechanism, not by wording. For each: the structural change, what it enables, why it should work, the main doubt, and the cheapest check. If the plain conventional answer is better, say so; a trade-off that reflects a real limit stays a trade-off.

## Subagents

Use them for a hard problem with separable parts, or when you want solution families that do not come from one line of thought: give two or three fresh agents the same step 1 and different operators, or different parts of the system, blind to each other. Agreement between them is not evidence. A small question stays in one agent. Offer `/idea-audit` when an idea is worth checking before anyone commits to it.
