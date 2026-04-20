"""
campus_nav.py
-------------
לוגיקת הניווט המרכזית של CampusNav.
מטפל בטעינת הנתונים, בניית הגרף, והפעלת אלגוריתם דייקסטרה.
"""

import pandas as pd
import networkx as nx
import os

# נתיב לתיקיית הנתונים (CSV-ים יושבים לידנו)
DATA_DIR = os.path.dirname(os.path.abspath(__file__))


# ──────────────────────────────────────────────
# טעינת הנתונים
# ──────────────────────────────────────────────

def load_data():
    """טוען את קבצי nodes.csv ו-edges.csv ומחזיר DataFrames."""
    nodes_path = os.path.join(DATA_DIR, "nodes.csv")
    edges_path = os.path.join(DATA_DIR, "edges.csv")
    nodes_df = pd.read_csv(nodes_path)
    edges_df = pd.read_csv(edges_path)
    return nodes_df, edges_df


# ──────────────────────────────────────────────
# בניית הגרף
# ──────────────────────────────────────────────

def build_graph(nodes_df, edges_df, weight="time"):
    """
    בונה גרף NetworkX לא-מכוּוָן ממושקל.

    פרמטרים:
        nodes_df  - DataFrame של צמתים
        edges_df  - DataFrame של קשתות
        weight    - 'time' (ברירת מחדל) או 'distance'

    מחזיר:
        G - גרף NetworkX
    """
    G = nx.Graph()

    # הוספת צמתים עם כל המאפיינים
    for _, row in nodes_df.iterrows():
        G.add_node(
            int(row["id"]),
            name=row["name"],
            floor=row["floor"],
            node_type=row["type"]
        )

    # הוספת קשתות עם שני משקלים (המשקל הפעיל לפי הפרמטר)
    for _, row in edges_df.iterrows():
        G.add_edge(
            int(row["source"]),
            int(row["target"]),
            distance=float(row["distance"]),
            time=float(row["time"]),
            weight=float(row[weight]),          # המשקל הפעיל לדייקסטרה
            source_type=row["source_type"],
            instruction=row.get("instruction", "המשך ישר")
        )

    return G


# ──────────────────────────────────────────────
# אלגוריתם דייקסטרה
# ──────────────────────────────────────────────

def find_shortest_path(G, source_id, target_id, weight="time"):
    """
    מפעיל דייקסטרה על הגרף G ומחזיר את המסלול הקצר ביותר.

    מחזיר dict עם:
        path        - רשימת מזהי הצמתים במסלול
        path_names  - רשימת שמות הצמתים
        total_time  - זמן כולל בשניות
        total_dist  - מרחק כולל במטרים
        found       - האם נמצא מסלול
        error       - הודעת שגיאה אם לא נמצא
    """
    if source_id == target_id:
        name = G.nodes[source_id]["name"]
        return {
            "path": [source_id],
            "path_names": [name],
            "total_time": 0,
            "total_dist": 0,
            "found": True,
            "error": None
        }

    try:
        path = nx.dijkstra_path(G, source_id, target_id, weight=weight)
    except nx.NetworkXNoPath:
        return {
            "path": [],
            "path_names": [],
            "total_time": 0,
            "total_dist": 0,
            "found": False,
            "error": f"לא קיים מסלול בין הצמתים {source_id} ל-{target_id}."
        }
    except nx.NodeNotFound as e:
        return {
            "path": [],
            "path_names": [],
            "total_time": 0,
            "total_dist": 0,
            "found": False,
            "error": f"צומת לא נמצא: {e}"
        }

    # חישוב סיכומי מרחק וזמן לאורך המסלול
    total_time = 0
    total_dist = 0
    for u, v in zip(path[:-1], path[1:]):
        edge_data = G[u][v]
        total_time += edge_data.get("time", 0)
        total_dist += edge_data.get("distance", 0)

    path_names = [G.nodes[n]["name"] for n in path]

    return {
        "path": path,
        "path_names": path_names,
        "total_time": total_time,
        "total_dist": total_dist,
        "found": True,
        "error": None
    }


# ──────────────────────────────────────────────
# פונקציות עזר
# ──────────────────────────────────────────────

def get_node_options(nodes_df):
    """מחזיר dict של {שם_תצוגה: id} לשימוש ב-selectbox של Streamlit."""
    options = {}
    for _, row in nodes_df.iterrows():
        floor_label = f"קומה {row['floor']}" if row['floor'] not in ("כל הקומות",) else row['floor']
        display = f"{row['name']}  [{floor_label}]"
        options[display] = int(row["id"])
    return options


def format_time(seconds):
    """ממיר שניות לפורמט קריא: 'X דקות Y שניות'."""
    seconds = int(seconds)
    minutes = seconds // 60
    secs = seconds % 60
    if minutes == 0:
        return f"{secs} שניות"
    if secs == 0:
        return f"{minutes} דקות"
    return f"{minutes} דקות {secs} שניות"


def get_graph_stats(G):
    """מחזיר נתוני סטטיסטיקה בסיסיים על הגרף."""
    return {
        "nodes": G.number_of_nodes(),
        "edges": G.number_of_edges(),
        "connected": nx.is_connected(G)
    }


# ──────────────────────────────────────────────
# בדיקת תקינות (ריצה ישירה)
# ──────────────────────────────────────────────

if __name__ == "__main__":
    print("טוען נתונים...")
    nodes_df, edges_df = load_data()

    print("בונה גרף...")
    G = build_graph(nodes_df, edges_df, weight="time")

    stats = get_graph_stats(G)
    print(f"\n── נתוני גרף ──")
    print(f"  צמתים  : {stats['nodes']}")
    print(f"  קשתות  : {stats['edges']}")
    print(f"  מחובר? : {'כן ✓' if stats['connected'] else 'לא ✗ — יש צמתים מנותקים'}")

    # בדיקת מסלולים לדוגמה
    test_cases = [
        (17, 28, "שער ראשי → c102"),
        (17, 47, "שער ראשי → ספריה"),
        (1,  47, "שער גבעת מרדכי → ספריה"),
        (16, 37, "שער בית הכרם → c202"),
    ]

    print(f"\n── בדיקות מסלולים ──")
    for src, tgt, label in test_cases:
        result = find_shortest_path(G, src, tgt, weight="time")
        if result["found"]:
            print(f"\n  {label}")
            print(f"  מסלול : {' → '.join(result['path_names'])}")
            print(f"  זמן   : {format_time(result['total_time'])}")
            print(f"  מרחק  : {result['total_dist']} מטר")
        else:
            print(f"\n  {label}")
            print(f"  שגיאה : {result['error']}")
