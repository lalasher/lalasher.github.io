# Guessing Game Flowchart

This flowchart represents the sequence of events in a guessing game where the user tries to guess a randomly generated number within a specified range.

## Flowchart
```mermaid
flowchart TD
    Start([Start]) --> GenerateRandom[Generate Random Number]
    GenerateRandom --> UserInput[Prompt User for Guess]
    UserInput --> ValidateInput{Is the Input Valid?}
    ValidateInput -->|Yes| CompareGuess[Compare Guess with Random Number]
    ValidateInput -->|No| InvalidInput[Prompt Invalid Input Message] --> UserInput
    CompareGuess -->|Too High| HighMessage[Display 'Too High'] --> UserInput
    CompareGuess -->|Too Low| LowMessage[Display 'Too Low'] --> UserInput
    CompareGuess -->|Correct| CorrectMessage[Display 'Correct!']
    CorrectMessage --> End([End])
