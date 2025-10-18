import plotly.graph_objects as go

"""
    ### TODO:
    ###     -Connect transaction data
    ###     -Create way to dynamically creates node labels and colors or setup prefined nodes and categorize transactions to these
    ###     -Sum transaction types
"""

def build_diagram():
    # Define the nodes dictionary
    # - 'label': List of node names (strings). Each entry corresponds to a node.
    # - 'color': List of colors for each node (strings, e.g., color names or hex codes).
    nodes = dict(
        label=["Income", "Misc Income", "Total Income", "Mortgage/Rent", "Utilities", "Groceries", "Fuel", "Insurance", "Restaurants", "Shopping", "Subscriptions", "Misc", "Total Liabilites", "Profit", ""],  # Set by providing a list of strings matching the number of nodes.
        color=["darkgreen", "darkgreen", "green", "yellow", "yellow", "yellow", "yellow", "yellow", "Red", "Red", "Red", "Red", "Red", "green", "lightgreen"]  # Set by providing a list of color strings, one per node.
    )

    # Define the links dictionary
    # - 'source': List of source node indices (integers, 0-based from nodes list).
    # - 'target': List of target node indices (integers).
    # - 'value': List of flow values (numbers, determine link widths).
    # - 'color': Optional list of colors for links (strings).
    links = dict(
        source=[0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14],  # Set by listing indices of sources for each link.
        target=[2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13],  # Set by listing indices of targets for each link.
        value=[800, 200, 300, 100, 100, 50, 50, 50, 50, 10, 10, 280, 300, 100, 100, 50, 50, 50, 50, 10, 10, 280],  # Set by listing numeric values for each link's flow.
        color=["lightgreen", "lightgreen", "red", "red", "red", "red", "red", "red", "red", "red", "red","lightgreen", "lightgreen", "red", "red", "red", "red", "red", "red", "red", "red", "red"]  # Set by providing colors per link (optional).
    )
    print(f"LENGTH Source: {len(links['source'])}")
    print(f"LENGTH target: {len(links['target'])}")
    print(f"LENGTH value: {len(links['value'])}")
    print(f"LENGTH color: {len(links['color'])}")

    # Create the Sankey trace
    # go.Sankey() creates the diagram object.
    # - node: Pass the nodes dict to configure nodes.
    # - link: Pass the links dict to configure flows.
    sankey = go.Sankey(
        node=nodes,  # Set by assigning the nodes dictionary.
        link=links   # Set by assigning the links dictionary.
    )

    # Create the figure
    # go.Figure() wraps the trace(s).
    fig = go.Figure(data=[sankey])  # Set data as a list containing the Sankey trace.

    # Update the layout
    # fig.update_layout() customizes the figure.
    # - title_text: String for the title.
    # - font_size: Integer for font size.
    fig.update_layout(
        title_text="Cashflow Sankey Diagram",  # Set by providing a string.
        font_size=10  # Set by providing an integer value.
    )

    # Save as HTML for offline viewing
    # fig.write_html() exports to an HTML file.
    # - Argument: File path string.
    # fig.write_html("cashflow_sankey.html")  # Set by specifying the output file name.
    fig.show()
