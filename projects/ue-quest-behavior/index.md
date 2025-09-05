---
title: Questing & Behavior Systems (UE)
layout: project
tags: [unreal, cpp]
parent: ue-gameplay-systems
demo: https://example.com
---

# Questing & Behavior Systems (UE5)

**TL;DR:** Composable quests with Behavior Tree integrations and reusable task library.

## Why
Designers wanted to craft complex quests without deep code knowledge and ensure AI behavior tied cleanly into quest states.

## What
- **Quest data:** modular objectives and rewards
- **Behavior Tree library:** reusable tasks and services
- **Designer tools:** Blueprint nodes and editor panels

## How (selected details)
- **Blackboard hooks:** quests update AI states via blackboards
- **Reusable tasks:** C++ base tasks for quick designer extension
- **Debugging:** on-screen quest state overlay for iteration

```cpp
// Example: tick a quest objective from a Behavior Tree task
void UBTTask_TickQuest::ExecuteTask(UBehaviorTreeComponent& OwnerComp) {
    QuestSubsystem->AdvanceObjective(QuestID, ObjectiveID);
}
```

## Outcome

* **Design velocity:** new quests built without engineering support
* **Consistency:** shared tasks reduced duplicated logic
* **Player engagement:** tighter AI integration improved quest responsiveness

