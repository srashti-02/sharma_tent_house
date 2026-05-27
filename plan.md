# PLAN.md

# 1. Three-Sentence Specification

This project is a command-line based rental management system for Sharma Tent House built using Python and JSON files.

Rakesh ji and Ankit will use the program to manage inventory, bookings, deliveries, returns, customer payments, damages, and item availability during busy wedding seasons.

The project will be considered complete when the system can safely store all business data, prevent booking mistakes, track rented items correctly, and support daily shop operations without depending on manual ledgers.

---

# 2. Information the Program Must Remember

The system must permanently store all important business data so that nothing is lost when the program closes.

## A. Inventory Items

The tent house has many kinds of rental items. Some items exist in large quantities like chairs and plates, while some are unique like LED walls or sound systems.

### Data to Store

* item_id (string)
* item_name (string)
* category (string)
* total_quantity (integer)
* rent_per_day (float)
* damage_charge (float)
* item_type (bulk / limited / unique)
* item_status (active/inactive)

### Unique Item Tracking

Unique and limited items such as LED Walls, DJ Systems, Sound Consoles, or Generator Sets must be tracked individually.

Each unique unit will have:

* unit_id (string)
* parent_item_id (string)
* serial_number (optional string)
* unit_status (available/booked/maintenance)

### Example Items

* Plastic Chair
* Round Table
* Pedestal Fan
* LED Wall
* Sofa Set
* Gas Burner
* Dinner Plate

### Reasoning

Availability should not be stored as a fixed number because item availability changes depending on overlapping booking dates. The system will calculate availability dynamically using delivery and return date ranges along with total inventory quantity.

Bulk items can use quantity-based tracking, while unique items require unit-level tracking so the same physical unit cannot be booked for multiple events at the same time.

---

## B. Customers

Customer information is needed for bookings, payments, and history tracking.

### Data to Store

* customer_id (string)
* customer_name (string)
* phone_number (string)
* address (string)
* customer_notes (optional string)
* total_bookings (integer)

### Reasoning

Customer history helps Rakesh ji identify trusted customers and frequent clients.

---

## C. Bookings

A booking stores all event-related information.

### Data to Store

* booking_id (string)
* customer_id (string)
* event_name (string)
* event_location (string)
* event_start_date (date)
* event_end_date (date)
* delivery_date (date)
* expected_return_date (date)
* booked_items (list)
* total_amount (float)
* deposit_paid (float)
* remaining_payment (float)
* payment_status (pending/partial/paid)
* booking_status (active/completed/cancelled)

### Booked Item Structure

For bulk items:

* item_id
* quantity
* price_per_day

For unique or limited items:

* item_id
* unit_id
* price_per_day

### Payment Logic

The booking record stores the money position before return processing.

* `total_amount` is the full quoted amount for the booking.
* `deposit_paid` is the advance collected at booking time.
* `remaining_payment` is the balance still due after deposit, before damage or missing-item adjustments.
* `payment_status` shows whether the customer has paid the quote fully, partially, or not yet.

### Availability Logic

Availability is calculated dynamically for a requested booking date range.

The system checks all existing bookings whose delivery and return dates overlap with the requested inventory movement window.

For bulk items:

available quantity = total quantity - overlapping booked quantity

For unique items:

the system checks whether a specific `unit_id` is already reserved during overlapping dates.

This prevents overbooking during peak wedding seasons when multiple events happen at the same time.

### Reasoning

Each booking can contain many items, so a list structure is necessary.

Date-range based availability checking is required to correctly handle overlapping bookings and real-world delivery schedules.

Unique items require unit-level tracking because the same physical LED Wall or Sound System cannot be sent to two different events at the same time.

The booking record should store only the pre-return money position. The final settlement belongs in the return record so the system has one clear place for “customer owes us” versus “refund due”.

---

## D. Returns and Damages

The program must track returned, damaged, and missing items.

### Data to Store

* return_id (string)
* booking_id (string)
* actual_return_date (date)
* returned_items (list)
* damaged_items (list)
* missing_items (list)
* late_fees (float)
* damage_total (float)
* missing_total (float)
* refundable_adjustments (float)
* booking_remaining_payment (float)
* final_balance (float)
* settlement_status (customer_owes/refund_due/settled)

### Final Settlement Logic

The return record stores the final money outcome after the event.

The system calculates:

final_balance = booking_remaining_payment + late_fees + damage_total + missing_total - refundable_adjustments

Meaning:

* If `final_balance > 0`, the customer still owes the shop.
* If `final_balance < 0`, the shop owes a refund to the customer.
* If `final_balance = 0`, the booking is fully settled.

### Reasoning

This helps calculate losses and customer dues correctly.

The booking section stores the pre-return balance, and the return section stores the final settlement. That keeps the money flow clear and prevents confusion between the quoted amount, the pending amount after advance, and the final amount after damages or refunds.

---

# 3. How the Groupings Connect

* Customers create bookings for events.
* Bookings reserve inventory items for delivery-to-return date ranges.
* Inventory availability is calculated by checking overlapping bookings.
* Bulk items are tracked using quantities.
* Unique items are tracked using unit_id values.
* Returned items complete the rental cycle.
* Damaged or missing items create extra charges for customers.
* Returns are directly connected to bookings.
* Customer payment records depend on booking totals, deposits, damages, late fees, and refund adjustments.

These connections are important because the entire business depends on inventory movement between customers and the shop.

---

# 4. File Structure

The program will use multiple JSON files instead of one large file.

## Files

* inventory.json
* customers.json
* bookings.json
* returns.json
* unique_units.json

Using separate files makes the system cleaner and easier to maintain.

---

## Example Inventory Record

```json
{
  "item_id": "I101",
  "item_name": "Plastic Chair",
  "category": "Furniture",
  "total_quantity": 500,
  "rent_per_day": 12,
  "damage_charge": 250,
  "item_type": "bulk"
}
```

---

## Example Unique Unit Record

```json
{
  "unit_id": "U501",
  "parent_item_id": "I301",
  "item_name": "LED Wall",
  "serial_number": "LED-7781",
  "unit_status": "available"
}
```

---

## Example Customer Record

```json
{
  "customer_id": "C201",
  "customer_name": "Rahul Agarwal",
  "phone_number": "9876543210",
  "address": "Talwandi, Kota"
}
```

---

## Example Booking Record

```json
{
  "booking_id": "B301",
  "customer_id": "C201",
  "event_name": "Agarwal Wedding",
  "event_start_date": "2026-12-18",
  "event_end_date": "2026-12-20",
  "delivery_date": "2026-12-17",
  "expected_return_date": "2026-12-21",
  "booked_items": [
    {
      "item_id": "I101",
      "quantity": 200,
      "price_per_day": 12
    },
    {
      "item_id": "I301",
      "unit_id": "U501",
      "price_per_day": 8000
    }
  ],
  "deposit_paid": 5000,
  "total_amount": 24000,
  "remaining_payment": 19000,
  "payment_status": "partial"
}
```

---

## Example Return Record

```json
{
  "return_id": "R401",
  "booking_id": "B301",
  "actual_return_date": "2026-12-21",
  "returned_items": [
    {
      "item_id": "I101",
      "quantity": 200
    },
    {
      "item_id": "I301",
      "unit_id": "U501"
    }
  ],
  "damaged_items": [],
  "missing_items": [],
  "late_fees": 0,
  "damage_total": 0,
  "missing_total": 0,
  "refundable_adjustments": 0,
  "booking_remaining_payment": 19000,
  "final_balance": 19000,
  "settlement_status": "customer_owes"
}
```

---

# 5. Operations

## Inventory Operations

1. Add new inventory item
2. Update inventory quantity
3. Add unique item unit
4. Update unit status
5. Remove inactive item
6. View all inventory items
7. Search item by name
8. Check item availability by date range

---

## Customer Operations

9. Add new customer
10. Search customer details
11. View customer booking history

---

## Booking Operations

12. Create new booking
13. Prevent overbooking automatically
14. Check overlapping bookings
15. Validate unique item availability
16. Edit existing booking
17. Cancel booking
18. Calculate booking amount
19. Record deposit payment
20. Show pending payment
21. Track delivery and expected return dates

---

## Delivery & Return Operations

22. View today’s deliveries
23. View today’s collections
24. Return rented items
25. Record damaged items
26. Record missing items
27. Add late return charges
28. Calculate final settlement

---

## Reporting Operations

29. Generate monthly revenue report
30. Generate damage/loss report
31. Show currently rented items
32. Show idle inventory items

---

## System Operations

33. Save data automatically
34. Load previous data at startup
35. Exit program safely

---

# 6. Things That Can Go Wrong

1. JSON file missing → create new file automatically.
2. Corrupted JSON file → restore backup/default file.
3. Invalid date format → ask user to re-enter date.
4. Negative quantity entered → reject input.
5. Negative payment entered → reject input.
6. Booking exceeds available quantity for requested dates → reject booking.
7. Booking ID already exists → generate new ID automatically.
8. Customer ID not found → show error message.
9. Returning more items than rented → block action.
10. Missing items detected → apply replacement charges.
11. Damaged items detected → apply damage fees.
12. Late return detected → add late charges.
13. Invalid menu option entered → show menu again.
14. Empty inventory booking attempt → reject booking.
15. Incorrect overlapping booking calculation → prevent confirmation.
16. Delivery date after expected return date → reject booking.
17. Same unique unit booked for overlapping dates → reject booking.
18. Unique unit marked under maintenance → block booking.
19. Final settlement mismatch after return update → recalculate from booking_remaining_payment and return charges.
20. User exits suddenly during save → create backup file.

---

# 7. One Thing I Don’t Know Yet

I still need to research and test the best way to efficiently calculate inventory availability across overlapping delivery and return date ranges during peak wedding season traffic, especially when both bulk inventory and individually tracked unique units are booked simultaneously.

Project plan completed successfully.
