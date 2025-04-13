---
followed by: "[[cybernetics]]"
is the study of:
  - "[[feedback]]"
  - "[[dynamical system]]"
instance of:
  - "[[systems engineering]]"
  - "[[area of mathematics]]"
topic's main template: "[[Template_Control theory]]"
maintained by WikiProject: "[[WikiProject Mathematics]]"
subclass of: "[[automatic control]]"
part of: "[[calculus of variations, systems theory and control theory]]"
Stack Exchange tag: https://stackoverflow.com/tags/control-theory
Commons gallery: Control theory
Commons category: Control theory
wikidata entity id: Q6501221
---
**Control theory** is a field of [control engineering](https://en.wikipedia.org/wiki/Control_engineering "Control engineering") and [applied mathematics](https://en.wikipedia.org/wiki/Applied_mathematics "Applied mathematics") that deals with the [control](https://en.wikipedia.org/wiki/Control_system "Control system") of [dynamical systems](https://en.wikipedia.org/wiki/Dynamical_system "Dynamical system") in engineered processes and machines. The objective is to develop a model or algorithm governing the application of system inputs to drive the system to a desired state, while minimizing any _delay_, _overshoot_, or _steady-state error_ and ensuring a level of control [stability](https://en.wikipedia.org/wiki/Stability_theory "Stability theory"); often with the aim to achieve a degree of [optimality](https://en.wikipedia.org/wiki/Optimal_control "Optimal control").

To do this, a **controller** with the requisite corrective behavior is required. This controller monitors the controlled [process variable](https://en.wikipedia.org/wiki/Process_variable "Process variable") (PV), and compares it with the reference or [set point](https://en.wikipedia.org/wiki/Setpoint_\(control_system\) "Setpoint (control system)") (SP). The difference between actual and desired value of the process variable, called the _error_ signal, or SP-PV error, is applied as feedback to generate a control action to bring the controlled process variable to the same value as the set point. Other aspects which are also studied are [controllability](https://en.wikipedia.org/wiki/Controllability "Controllability") and [observability](https://en.wikipedia.org/wiki/Observability "Observability"). Control theory is used in [control system engineering](https://en.wikipedia.org/wiki/Control_system_engineering "Control system engineering") to design automation that have revolutionized manufacturing, aircraft, communications and other industries, and created new fields such as [robotics](https://en.wikipedia.org/wiki/Robotics "Robotics").

Extensive use is usually made of a diagrammatic style known as the [block diagram](https://en.wikipedia.org/wiki/Block_diagram "Block diagram"). In it the [transfer function](https://en.wikipedia.org/wiki/Transfer_function "Transfer function"), also known as the system function or network function, is a mathematical model of the relation between the input and output based on the [differential equations](https://en.wikipedia.org/wiki/Differential_equation "Differential equation") describing the system.

## Open-loop and closed-loop (feedback) control



Fundamentally, there are two types of control loop: _[open-loop control](https://en.wikipedia.org/wiki/Open-loop_control "Open-loop control")_ (feedforward), and _[closed-loop control](https://en.wikipedia.org/wiki/Closed-loop_control "Closed-loop control")_ (feedback).

- In open-loop control, the control action from the controller is independent of the "process output" (or "controlled process variable"). A good example of this is a central heating boiler controlled only by a timer, so that heat is applied for a constant time, regardless of the temperature of the building. The control action is the switching on/off of the boiler, but the controlled variable should be the building temperature, but is not because this is open-loop control of the boiler, which does not give closed-loop control of the temperature.
- In closed loop control, the control action from the controller is dependent on the process output. In the case of the boiler analogy, this would include a thermostat to monitor the building temperature, and thereby feed back a signal to ensure the controller maintains the building at the temperature set on the thermostat. A closed loop controller therefore has a feedback loop which ensures the controller exerts a control action to give a process output the same as the "reference input" or "set point". For this reason, closed loop controllers are also called feedback controllers.[11](app://obsidian.md/11)(#cite_note-Control_loop_auto-11)