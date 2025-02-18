# Filename: main.py (or any file of your choice)
# -----------------------------------------------------------------------------
# DISCLAIMER:
# This code is an EXAMPLE solution for reference/study purposes ONLY.
# Submitting it as your own may violate assignment rules against plagiarism
# or AI-generated solutions. Use it ethically and responsibly.
# -----------------------------------------------------------------------------

def get_free_tables(tables):
    """
    Level 1
    Returns a list of table IDs (or entire objects) that are currently free.
    """
    free_tables = []
    for table in tables:
        if not table["occupied"]:  # occupied == False
            free_tables.append(table["table_id"])
    return free_tables


def find_one_table_for_size(tables, party_size):
    """
    Level 2
    Returns the first table ID that can seat 'party_size' and is free,
    or None if none found.
    """
    for table in tables:
        if not table["occupied"] and table["capacity"] >= party_size:
            return table["table_id"]
    return None


def find_all_tables_for_size(tables, party_size):
    """
    Level 3
    Returns a list of all table IDs that can seat 'party_size' and are free.
    """
    suitable_tables = []
    for table in tables:
        if not table["occupied"] and table["capacity"] >= party_size:
            suitable_tables.append(table["table_id"])
    return suitable_tables


def find_tables_including_combos(tables, party_size):
    """
    Level 4
    Returns a list of table or table combinations that can seat 'party_size'.
    Adjacent combos are determined via the table's "neighbors" list.
    
    Example output structure:
    [(1,), (3,), (1,2), (3,5)]  # Each tuple is a single table or a pair.
    """
    results = []

    for table in tables:
        # Check single table
        if (not table["occupied"]) and (table["capacity"] >= party_size):
            results.append((table["table_id"],))
        
        # Check neighbor combos if single table can't seat them
        if table["neighbors"] and not table["occupied"]:
            for neighbor_id in table["neighbors"]:
                neighbor_table = next((t for t in tables if t["table_id"] == neighbor_id), None)
                
                # If neighbor also exists, is free, and combined capacity meets needs
                if neighbor_table and (not neighbor_table["occupied"]):
                    total_capacity = table["capacity"] + neighbor_table["capacity"]
                    if total_capacity >= party_size:
                        # Sort to avoid duplicates like (1,2) and (2,1)
                        combo = tuple(sorted([table["table_id"], neighbor_table["table_id"]]))
                        if combo not in results:
                            results.append(combo)
    
    return results


def friendly_output(tables, combos):
    """
    Bonus:
    Takes the combos from Level 4 (like [(1,), (2,), (1,2)]) and
    prints a more user-friendly message about each result.
    """
    for group in combos:
        if len(group) == 1:
            # Single table
            table_id = group[0]
            tdata = next((t for t in tables if t["table_id"] == table_id), None)
            if tdata:
                print(f"Table {table_id} is free and can seat {tdata['capacity']} people.")
        else:
            # Combined tables
            t1_id, t2_id = group
            t1_data = next((t for t in tables if t["table_id"] == t1_id), None)
            t2_data = next((t for t in tables if t["table_id"] == t2_id), None)
            if t1_data and t2_data:
                total_capacity = t1_data["capacity"] + t2_data["capacity"]
                print(f"Tables {t1_id} and {t2_id} together can seat {total_capacity} people.")


# -----------------------------------------------------------------------------
# Example usage / testing:
if __name__ == "__main__":
    # Example data
    tables_data = [
        {"table_id": 1, "capacity": 2, "occupied": False, "neighbors": [2]},
        {"table_id": 2, "capacity": 4, "occupied": True,  "neighbors": [1, 3]},
        {"table_id": 3, "capacity": 2, "occupied": False, "neighbors": [2, 4]},
        {"table_id": 4, "capacity": 6, "occupied": False, "neighbors": [3]}
    ]

    print("LEVEL 1: Free Tables =", get_free_tables(tables_data))

    print("LEVEL 2: One table for party size 2 =", find_one_table_for_size(tables_data, 2))

    print("LEVEL 3: All tables for party size 2 =", find_all_tables_for_size(tables_data, 2))

    combos = find_tables_including_combos(tables_data, 5)
    print("LEVEL 4: Single or combined tables for party size 5 =", combos)

    print("\nBONUS: Friendly output for the combos above")
    friendly_output(tables_data, combos)
