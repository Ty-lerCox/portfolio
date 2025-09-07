---
layout: post
title: "Political System"
date: 2025-04-05 00:00:00 +0000
categories: [CityRPG]
tags:
  - CityRPG
  - Politics
  - Elections
  - Mayor
  - Taxes
  - Economy
---

CityRPG features an in-game political layer where players campaign for office, set city policy, and keep the economy running. This post explains how elections work, what powers leaders hold, and how citizens can keep their government in check.

> Add a header image
> `![Town hall and campaign posters](path-or-url-to-image)`

---

## Elections

- **When they occur**: Elections may trigger automatically when enough players are online or can be started manually by the server.
- **Running**: Use the Town Hall interface or `/election run` to enter the race. There is usually a fee to discourage spam candidates.
- **Voting**: Once the election period opens, players cast votes via UI or `/election vote <name>`. Highest votes wins.
- **Term**: The winner becomes city leader (mayor) until impeached, removed, or a new election is held.

> `![Voting booth or ballot UI](image-url)`

---

## Leadership Powers

- **Set Taxes**: Leaders can adjust city tax rates affecting property, sales, and payroll. Use `/economy tax <value>` or in-game menus.
- **Manage Budget**: City funds collected from taxes and fines can be allocated to events or infrastructure.
- **Post Contracts & Policies**: Leaders may post city contracts (`/citycontractpost`) or modify policies that influence gameplay loops.
- **Economy Modifier**: Leaders can influence the live economy percentage via donations or certain policies, shifting payouts up or down.

> `![Mayor office and policy screen](image-url)`

---

## Taxes & City Funds

- **Sources**: Income flows from sales cuts, fines, and donation commands like `/donate <amount>`.
- **Usage**: Funds can seed events, pay bounties, or buffer the city economy.
- **Transparency**: Players can check city status with `/city` or `/economy` to see current rates and balances.

---

## Impeachment & Accountability

- **Impeach Command**: Unhappy citizens can call `/impeach` to start a removal vote. A majority ousts the current leader.
- **Auto-Removal**: Leaders may also be removed for inactivity or poor approval depending on server rules.
- **Checks & Balances**: Regular elections and open commands ensure no one holds power indefinitely.

> `![Citizens protesting at town hall](image-url)`

---

## Useful Commands

- `/election run`, `/election vote <name>` – participate in elections.
- `/economy`, `/economy tax <value>` – view or adjust the economy and tax rate (leader only).
- `/city` – view current city funds and policy summary.
- `/impeach` – call for a vote to remove the current leader.
- `/donate <amount>` – contribute to the city economy.

---

## FAQ

- **Can anyone run for office?**
  Yes, as long as you pay the entry fee and the election is active.
- **Do taxes affect all income?**
  Taxes typically apply to sales, payroll, and property; check `/city` for specifics.
- **What happens to city funds?**
  Leaders can allocate funds for events or bonuses; unspent money carries over to the next administration.

Add screenshots of election posters, the mayor’s office, and economic graphs to make the political system feel alive.

