---
layout: post
title: 'Unified Process Overview'
date: 2025-04-20 00:00:00 +0000
pin: true
categories: [Unified Process]
tags:
    - Angular
    - Signals
    - NgRx
    - Logistics
    - Workflow
    - CDC
    - Kafka
    - Grafana
    - Prometheus
    - Loki
    - Tempo
    - Keycloak
    - Kubernetes
    - Ansible
    - DORA
---

_Unified Process_ is a step‑centric platform for logistics workflows. Instead of relying solely on event streams, it models each business process as an explicit sequence of **steps**, **transitions**, and **guards**—making state changes observable, testable, and easier to recover when things go wrong. The front end is built with Angular (Signals + NgRx), with deep instrumentation across the stack.

![Process orchestration banner](https://placehold.co/600x400?text=Placeholder&format=svg)

---

## Introduction

Unified Process is:

-   **A Step‑Centric Orchestrator** — represents logistics flows as deterministic state machines (steps → transitions → effects).
-   **A Front‑End for Operators** — Angular UI surfaces the current step, blockers, SLAs, and remediation actions.
-   **An Observability‑First System** — traces, metrics, and logs tie every step to its upstream/downstream services.

![Operator console showing step timeline](https://placehold.co/600x400?text=Placeholder&format=svg)

---

## Why Step‑Centric (vs. Event‑Only)?

Event buses are great at decoupling producers and consumers, but complex operations can drift when state is implied by “latest events.” A step‑centric model:

-   **Makes intent explicit** (what step we _must_ reach next).
-   **Improves debuggability** (you can ask: _which entities are stuck in Step X?_).
-   **Enables safe retries/compensation** at the step boundary.
-   **Clarifies SLAs** by measuring dwell time per step.

---

## Core Concepts

-   **Process**: Named workflow (e.g., _Shipment Lifecycle_).
-   **Step**: A durable state with entry/exit criteria.
-   **Transition**: Movement between steps when **guards** pass.
-   **Guards**: Boolean checks (data present, validations complete, external ACK received).
-   **Effects**: Side‑effects on transition (emit command, write record, notify, update index).

![State machine sketch: Received → Validated → Booked → Dispatched → Delivered](https://placehold.co/600x400?text=Placeholder&format=svg)

Example (illustrative YAML‑style):

```yaml
process: ShipmentLifecycle
steps:
    - name: Received
      exitWhen:
          - docs.validated == true
      onExit:
          - emit: ValidateDocs
    - name: Validated
      exitWhen:
          - carrier.booking.confirmed == true
      onExit:
          - emit: BookCarrier
    - name: Booked
      exitWhen:
          - dispatch.window.open == true
      onExit:
          - emit: Dispatch
    - name: Dispatched
      exitWhen:
          - pod.received == true
      onExit:
          - emit: ConfirmDelivery
    - name: Delivered
      terminal: true
```
