from categories import CATEGORIES

class Category:
    def  __init__(self, label, source, sums):
        self.label = label
        self.source = source
        self.node_color = self.get_node_color(label)
        self.sources,self.targets,self.values,self.link_colors = self.get_sources_targets_values_colors(source, label, sums)
        
        
    def get_node_color(self, label):
        if ("income" in label.lower()
            or "savings" in label.lower()
        ):
            return "#00FF00"
        else:
            return "#FF0000"
        
    def get_sources_targets_values_colors(self, source, label, sums):
        sources = []
        targets = []
        link_colors = []
        values = []
        match label:
            case "Income" | "Misc Income":
                sources.append(source)
                targets.append(CATEGORIES.index("Total Income"))
                values.append(float(sums[label]))
                link_colors.append("#90EE90")
                return sources,targets,values,link_colors
            case "Total Income":
                if sums["Savings"] > 0:
                    sources.append(source)
                    targets.append(CATEGORIES.index("Savings"))
                    values.append(float(sums["Savings"]))
                    link_colors.append("#90EE90")
                    sources.append(source)
                    targets.append(CATEGORIES.index("Total Liabilities"))
                    values.append(float(sums["Total Liabilities"]))
                    link_colors.append("#FF9999")
                else:
                    sources.append(source)
                    targets.append(CATEGORIES.index("Total Liabilities"))
                    values.append(float(sums["Total Income"]))
                    link_colors.append("#FF9999")
                return sources,targets,values,link_colors
            case "Total Liabilities":
                sources.append(source)
                targets.append(CATEGORIES.index("Mortgage/Rent"))
                values.append(float(sums["Mortgage/Rent"]))
                link_colors.append("#FF9999")
                sources.append(source)
                targets.append(CATEGORIES.index("Utilities"))
                values.append(float(sums["Utilities"]))
                link_colors.append("#FF9999")
                sources.append(source)
                targets.append(CATEGORIES.index("Groceries"))
                values.append(float(sums["Groceries"]))
                link_colors.append("#FF9999")
                sources.append(source)
                targets.append(CATEGORIES.index("Fuel"))
                values.append(float(sums["Fuel"]))
                link_colors.append("#FF9999")
                sources.append(source)
                targets.append(CATEGORIES.index("Insurance"))
                values.append(float(sums["Insurance"]))
                link_colors.append("#FF9999")
                sources.append(source)
                targets.append(CATEGORIES.index("Restaurants"))
                values.append(float(sums["Restaurants"]))
                link_colors.append("#FF6666")
                sources.append(source)
                targets.append(CATEGORIES.index("Shopping"))
                values.append(float(sums["Shopping"]))
                link_colors.append("#FF6666")
                sources.append(source)
                targets.append(CATEGORIES.index("Subscriptions"))
                values.append(float(sums["Subscriptions"]))
                link_colors.append("#FF6666")
                sources.append(source)
                targets.append(CATEGORIES.index("Misc"))
                values.append(float(sums["Misc"]))
                link_colors.append("#FF6666")
                return sources,targets,values,link_colors
            case "Savings":
                if sums["Savings"] < 0:
                    sources.append(source)
                    targets.append(CATEGORIES.index("Total Liabilities"))
                    values.append(float(abs(sums["Savings"])))
                    link_colors.append("#FF6666")
                return sources,targets,values,link_colors
            # case _:
            #     sources.append(source)
            #     targets.append(CATEGORIES.index("Total Liabilities"))
            #     values.append(float(sums[label]))
            #     if label in CATEGORIES[5:10]:
            #         link_colors.append("#FF9999")
            #     else:
            #         link_colors.append("#FF6666")
            #     return sources,targets,values,link_colors
        return sources,targets,values,link_colors

    def __repr__(self):
        return (
            f"""Category data: 
            {self.label}, 
            {self.node_color}, 
            {self.source}, 
            {self.sources}, 
            {self.targets}, 
            {self.values}, 
            {self.link_colors}"""
            )