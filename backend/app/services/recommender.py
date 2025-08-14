def suggest_upsell(order_items):
    """Simple rule-based upsell: if burger → suggest fries & drink upsize"""
    upsells = []
    item_ids = [i.item_id if hasattr(i, 'item_id') else i.get('item_id') for i in order_items]

    if any("burger" in i for i in item_ids) and "fries" not in item_ids:
        upsells.append({"item_id": "fries", "suggestion": "Add fries for ₱50?"})

    if any("cola" in i or "drink" in i for i in item_ids):
        upsells.append({"item_id": "drink_large", "suggestion": "Upsize your drink for ₱20?"})

    return upsells
