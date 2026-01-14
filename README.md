This is a project I made during high school. Due to limitations of my abilities back then, this was not made compatible on other user's computers. See docs/IA-Crit-D for the project in action. 
# Airplane Boarding & Seating Optimization  
**Genetic Algorithms + Cellular Automata**

This project studies how airplane seating distribution and boarding order can be optimized to reduce boarding time and close passenger contact, motivated by COVID-19 transmission risk during air travel.

The final product is a desktop application that:
- Computes an optimal seating plan using a genetic algorithm
- Simulates and compares real-world boarding strategies using cellular automata
- Produces visual outputs (seat maps and boarding videos) to make results interpretable

The work combines probability, simulation, and optimization, and was developed with direct feedback from an industry client.

---

## Project Structure

    .
    ├── code/
    │   ├── Main.py                # GUI entry point
    │   ├── GA.py                  # Seating optimization interface
    │   ├── CA.py                  # Boarding simulation interface
    │   ├── cellular.py            # Cellular automata engine
    │   ├── datastructures.py      # Java–Python bridge (JPype)
    │   └── IA.jar                 # Java genetic algorithm backend
    │
    ├── docs/
    │   ├── IA-Crit-A.pdf          # Problem definition & rationale
    │   ├── IA-Crit-B-Design.pdf   # System & algorithm design
    │   ├── IA-Crit-C.pdf          # Technical algorithm explanation
    │   ├── IA-Crit-E.pdf          # Testing & evaluation
    │   ├── IA-Appendix-1.pdf      # Research & client communication
    │   └── IA-Appendix-2.pdf      # Code documentation
    │
    └── README.md

---

## Documentation Guide

### Problem Motivation  
See `docs/IA-Crit-A.pdf` for background, client requirements, and success criteria.

### Design and Architecture  
See `docs/IA-Crit-B-Design.pdf` for system design, UML diagrams, and flowcharts.

### Core Algorithms  
See `docs/IA-Crit-C.pdf` for detailed explanations of:
- Genetic algorithm for seating optimization
- Cellular automata boarding simulation
- Mathematical modeling and parameterization

### Code Reference  
See `docs/IA-Appendix-2.pdf` for file-by-file implementation details.

### Research Process  
See `docs/IA-Appendix-1.pdf` for literature review and client feedback.

### Testing and Evaluation  
See `docs/IA-Crit-E.pdf` for validation against success criteria and limitations.

---

## Running the Application

### Requirements
- Python 3.8+
- Java JDK
- Python libraries:
  - numpy
  - matplotlib
  - moviepy
  - jpype
  - tkinter

### Launch
Run the following from the project root:

    python Main.py

---

## Scope and Future Work

The GUI is functional but minimal. Future improvements could include:
- Cross-platform support
- Improved UI/UX
- Mobile deployment
- Alternative visualization backends

---

## Author

Haipeng (Eric) Chang  
Math & Physics  
University of Toronto
