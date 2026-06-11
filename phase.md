# PHASE.md

# Phase 1 — Inventory Foundation (The Smallest Useful Program)

## Goal

Build the smallest useful version of the tent house management system that works end-to-end and persists data between runs.

At the end of this phase, Rakesh ji should be able to maintain the shop inventory without using a paper register.

---

## Features

### Inventory Management

* Add inventory item
* View inventory items
* Search inventory item by name
* Update inventory quantity
* Mark item active/inactive

### Data Persistence

* Store inventory data in inventory.json
* Automatically load saved inventory on startup
* Automatically save changes

### Validation

* Prevent negative quantities
* Prevent empty item names
* Prevent duplicate item IDs

---

## Files

* inventory.json

---

## Tests

* Add item and restart program → data still exists
* Update quantity and restart program → updated value remains
* Search existing item
* Reject invalid quantity
* Reject duplicate ID

---

## Deliverable

A complete inventory management CLI that permanently remembers stock and can be demonstrated in less than two minutes.

---

# Phase 2 — Availability Engine (The Core Business Problem)

## Goal

Solve the most important technical problem in the entire project:

"Can an item be rented during a given date range?"

This phase focuses entirely on availability calculation before adding the complexity of customers, payments, or returns.

---

## Features

### Booking Prototype

For a single inventory item:

* Create booking
* Store delivery date
* Store return date
* Reserve quantity

### Availability Calculation

For bulk inventory:

* Detect overlapping date ranges
* Calculate remaining available quantity

For unique inventory:

* Detect unit conflicts
* Prevent double booking

### Availability Checker

User can enter:

* item
* quantity
* date range

System returns:

* Available
* Not available
* Remaining quantity

---

## Files

* inventory.json
* bookings.json
* unique_units.json

---

## Tests

### Bulk Item

Total chairs = 500

Booking A:
200 chairs
1 Jan – 3 Jan

Booking B:
250 chairs
2 Jan – 4 Jan

Result:
50 chairs available

Booking C:
100 chairs
2 Jan – 4 Jan

Result:
Rejected

### Unique Item

LED Wall U501

Booking A:
1 Jan – 3 Jan

Booking B:
2 Jan – 4 Jan

Result:
Rejected

---

## Deliverable

A proven availability engine that prevents overbooking and correctly handles overlapping dates.

---

# Phase 3 — Complete Rental Operations

## Goal

Expand the availability system into a real tent-house booking workflow.

At the end of this phase, the shop can run normal rental operations.

---

## Phase 3A — Customer Management

### Features

* Add customer
* Search customer
* View customer history

## Phase 3 Completion Rules

Each sub-phase must remain independently runnable and demoable.

### Phase 3A Done When

- Customer records can be added, searched, and persisted.
- Program runs successfully without booking functionality.
- Customer data survives restart.

### Phase 3B Done When

- Customers can create bookings.
- Multiple items can be added to a booking.
- Availability checks work correctly.
- Program remains runnable without payment features.

### Phase 3C Done When

- Booking totals are calculated.
- Deposits can be recorded.
- Remaining balances are calculated.
- Discounts and negotiated pricing are stored separately from standard rates.

### Phase 3D Done When

- Today's deliveries can be listed.
- Today's collections can be listed.
- Active bookings can be viewed.
- Currently rented inventory can be displayed.

Each sub-phase must be demonstrable without requiring later Phase 3 features.

### Files

* customers.json

---

## Phase 3B — Full Booking Workflow

### Features

* Create booking
* Multiple items per booking
* Bulk item booking
* Unique item booking
* Edit booking
* Cancel booking

### Booking Data

* Customer
* Event details
* Delivery date
* Return date
* Item list

---

## Phase 3C — Pricing & Payments

### Features

* Standard pricing
* Negotiated pricing
* Discounts
* Deposit payment
* Remaining payment calculation
* Payment status tracking

---

## Phase 3D — Daily Operations

### Features

* Today's deliveries
* Today's collections
* Active bookings
* Currently rented inventory

---

## Tests

* Multi-item booking
* Discount booking
* Deposit calculations
* Booking cancellation
* Active rental tracking

---

## Deliverable

A working business system capable of handling normal day-to-day tent house operations.

---

# Phase 4 — Returns, Damages & Wedding Season Stress Testing

## Goal

Handle everything that goes wrong during a busy wedding season.

This phase focuses on real-world failures and edge cases.

---

## Features

### Return Processing

* Return booking
* Record actual return date
* Update inventory state

### Damage Handling

* Damaged quantity
* Damage charges

### Missing Items

* Missing quantity
* Replacement charges

### Late Returns

* Detect delay
* Apply late fees

### Final Settlement

Calculate:

* Remaining payment
* Damage fees
* Missing charges
* Late fees
* Refund adjustments

---

## Stress Testing

### Business Scenarios

* Multiple overlapping weddings
* Partial item returns
* Lost inventory
* Damaged inventory
* Customer cancellation
* Maintenance units unavailable
* Very large bookings
* Consecutive bookings on nearby dates

### System Scenarios

* Missing JSON file
* Corrupted JSON file
* Invalid dates
* Invalid IDs
* Unexpected program exit

---

## Deliverable

A system that survives real wedding-season conditions without losing data or producing incorrect inventory counts.

---

# Phase 5 — Reporting, Refactoring & Handover Quality

## Goal

Transform working code into software that is easy to maintain, understand, and hand over.

---

## Features

### Reports

* Monthly revenue report
* Damage report
* Missing inventory report
* Discount usage report
* Idle inventory report

### Code Improvements

* Refactor repeated logic
* Improve module structure
* Improve naming consistency
* Improve documentation

### User Experience

* Cleaner CLI menus
* Better error messages
* Easier navigation
* Confirmation prompts

### Project Documentation

* README update
* Installation guide
* Usage guide
* Example workflows

### Final Testing

* Full booking lifecycle test
* Full return lifecycle test
* Persistence verification
* End-to-end business simulation

---

## Deliverable

A polished, maintainable tent-house rental management system that Rakesh ji can realistically use and another developer can easily understand.



