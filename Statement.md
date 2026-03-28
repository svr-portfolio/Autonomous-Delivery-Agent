## Problem Statement

Delivery agents often face difficulty in determining the most cost-efficient and time-saving route to reach a destination. In real-world scenarios, environments are dynamic, with obstacles that may appear, disappear, or move over time. Traditional static pathfinding approaches fail to adapt to such changes, leading to inefficient routing and increased delivery time.

This project aims to address this problem by implementing intelligent pathfinding algorithms that can efficiently compute optimal paths and dynamically adapt to changing environments.


## Scope of the Project

The scope of this project is to design and implement a grid-based environment in which an agent navigates from a start position to a goal position. The system demonstrates and compares various pathfinding algorithms such as **Breadth-First Search (BFS)**, **Uniform Cost Search (UCS)**, and **A\***.

The project incorporates both static and dynamic obstacles to simulate real-world conditions. It also enables the agent to replan its path whenever the current path becomes blocked, ensuring robustness and adaptability.


## Target Users

- Students studying artificial intelligence and algorithms  
- Office workers involved in logistics and planning  
- Residents using delivery services for food, groceries, or documents  


## High-Level Features

### 1. Grid-Based Environment
- Creates a virtual grid world  
- Includes obstacles and navigable paths  
- Defines start and goal positions  

### 2. Dynamic Obstacles
- Introduces moving obstacles  
- Simulates real-world unpredictability  

### 3. Pathfinding Algorithms
- Implements BFS, UCS, and A*  
- Finds efficient paths from start to goal  

### 4. Adaptive Replanning
- Recalculates path when blocked  
- Ensures continuous movement toward the goal  

### 5. Performance Comparison
- Compares algorithms based on:
  - Execution time  
  - Nodes explored  
  - Overall efficiency  
