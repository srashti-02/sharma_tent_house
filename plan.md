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
* available_quantity (integer)
* rent_per_day (float)
* damage_charge (float)
* item_type (bulk / limited / unique)
* item_status (active/inactive)

### Example Items

* Plastic Chair
* Round Table
* Pedestal Fan
* LED Wall
* Sofa Set
* Gas Burner
* Dinner Plate

### Reasoning

Tracking both total quantity and available quantity makes availability checking faster and simpler.

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
* booking_start_date (date)
* booking_end_date (date)
* booked_items (list)
* total_amount (float)
* deposit_paid (float)
* remaining_payment (float)
* booking_status (active/completed/cancelled)

### Booked Item Structure

Each booked item contains:

* item_id
* quantity
* price_per_day

### Reasoning

Each booking can contain many items, so a list structure is necessary.

---

## D. Returns and Damages

The program must track returned, damaged, and missing items.

### Data to Store

* return_id (string)
* booking_id (string)
* returned_items (list)
* damaged_items (list)
* missing_items (list)
* late_fees (float)
* damage_total (float)
* final_balance (float)

### Reasoning

This helps calculate losses and customer dues correctly.

---

# 3. How the Groupings Connect

* Customers create bookings for events.
* Bookings reserve inventory items for specific dates.
* Inventory quantity decreases when a booking is confirmed.
* Returned items increase inventory quantity again.
* Damaged or missing items create extra charges for customers.
* Returns are directly connected to bookings.
* Customer payment records depend on booking totals, deposits, damages, and late fees.

These connections are important because the entire business depends on inventory movement between customers and the shop.

---

# 4. File Structure

The program will use multiple JSON files instead of one large file.

## Files

* inventory.json
* customers.json
* bookings.json
* returns.json

Using separate files makes the system cleaner and easier to maintain.

---

## Example Inventory Record

```json id="zku982"
{
  "item_id": "I101",
  "item_name": "Plastic Chair",
  "category": "Furniture",
  "total_quantity": 500,
  "available_quantity": 320,
  "rent_per_day": 12,
  "damage_charge": 250,
  "item_type": "bulk"
}
```

---

## Example Customer Record

```json id="vfi734"
{
  "customer_id": "C201",
  "customer_name": "Rahul Agarwal",
  "phone_number": "9876543210",
  "address": "Talwandi, Kota"
}
```

---

## Example Booking Record

```json id="owx661"
{
  "booking_id": "B301",
  "customer_id": "C201",
  "event_name": "Agarwal Wedding",
  "booking_start_date": "2026-12-18",
  "booking_end_date": "2026-12-20",
  "booked_items": [
    {
      "item_id": "I101",
      "quantity": 200,
      "price_per_day": 12
    }
  ],
  "deposit_paid": 5000,
  "total_amount": 24000
}
```

---

# 5. Operations

## Inventory Operations

1. Add new inventory item
2. Update inventory quantity
3. Remove inactive item
4. View all inventory items
5. Search item by name
6. Check item availability by date

---

## Customer Operations

7. Add new customer
8. Search customer details
9. View customer booking history

---

## Booking Operations

10. Create new booking
11. Prevent overbooking automatically
12. Edit existing booking
13. Cancel booking
14. Calculate booking amount
15. Record deposit payment
16. Show pending payment

---

## Delivery & Return Operations

17. View today’s deliveries
18. View today’s collections
19. Return rented items
20. Record damaged items
21. Record missing items
22. Add late return charges

---

## Reporting Operations

23. Generate monthly revenue report
24. Generate damage/loss report
25. Show currently rented items
26. Show idle inventory items

---

## System Operations

27. Save data automatically
28. Load previous data at startup
29. Exit program safely

---

# 6. Things That Can Go Wrong

1. JSON file missing → create new file automatically.
2. Corrupted JSON file → restore backup/default file.
3. Invalid date format → ask user to re-enter date.
4. Negative quantity entered → reject input.
5. Negative payment entered → reject input.
6. Booking exceeds available quantity → reject booking.
7. Booking ID already exists → generate new ID automatically.
8. Customer ID not found → show error message.
9. Returning more items than rented → block action.
10. Missing items detected → apply replacement charges.
11. Damaged items detected → apply damage fees.
12. Late return detected → add late charges.
13. Invalid menu option entered → show menu again.
14. Empty inventory booking attempt → reject booking.
15. Booking dates overlap incorrectly → prevent confirmation.
16. User exits suddenly during save → create backup file.

---

# 7. One Thing I Don’t Know Yet

I still need to research and test the best way to calculate inventory availability when many bookings overlap across different dates, especially during peak wedding season when multiple events happen at the same time.

Project plan completed successfully.