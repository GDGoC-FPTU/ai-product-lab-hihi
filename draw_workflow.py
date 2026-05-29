import os
import sys
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Force UTF-8 encoding for output
if sys.stdout.encoding != 'utf-8':
    try:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    except Exception:
        pass

def draw_workflow():
    fig, ax = plt.subplots(figsize=(14, 6.5))

    # Set background to white
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    # Define steps of Vinhomes manual workflow in clean English
    steps = [
        {
            "num": "1",
            "title": "Submit Feedback",
            "actor": "Resident",
            "time": "1 min",
            "tag": "",
            "desc": "Sends text/photos\nvia Resident App",
            "bottleneck": False
        },
        {
            "num": "2",
            "title": "Read & Analyze",
            "actor": "CS Operator",
            "time": "4 mins",
            "desc": "Reads content &\nverifies legitimacy",
            "bottleneck": False
        },
        {
            "num": "3",
            "title": "Categorize Ticket",
            "actor": "CS Operator",
            "time": "4 mins",
            "tag": "[BOTTLENECK]",
            "desc": "Manually identifies dept\n(electric, water, security)",
            "bottleneck": True
        },
        {
            "num": "4",
            "title": "Route Ticket",
            "actor": "CS -> Tech Team",
            "time": "3 mins",
            "tag": "[HANDOFF + BOTTLENECK]",
            "desc": "Manually forwards details\nto building technician",
            "bottleneck": True
        },
        {
            "num": "5",
            "title": "Dispatch & Solve",
            "actor": "Technician",
            "time": "1 min",
            "tag": "",
            "desc": "Receives ticket &\nfixes issue on-site",
            "bottleneck": False
        }
    ]

    box_width = 2.2
    box_height = 1.5
    y_pos = 2.0

    # Draw each box and arrow
    for i, step in enumerate(steps):
        # Calculate x position with spacing
        x_pos = 0.3 + i * 2.65
        
        # Determine colors based on bottleneck status
        if step["bottleneck"]:
            edgecolor = '#e74c3c'  # Crimson red for bottleneck
            facecolor = '#fdf2e9'  # Very light orange-red
            linewidth = 2.5
        else:
            edgecolor = '#3498db'  # Ocean blue
            facecolor = '#ebf5fb'  # Very light blue
            linewidth = 1.8
            
        # Draw fancy rounded box
        rect = patches.FancyBboxPatch(
            (x_pos, y_pos), box_width, box_height,
            boxstyle="round,pad=0.08",
            facecolor=facecolor, edgecolor=edgecolor, linewidth=linewidth
        )
        ax.add_patch(rect)
        
        # 1. Step label header (y = 3.3)
        ax.text(x_pos + box_width/2, y_pos + 1.3, f"Step {step['num']}", 
                ha='center', va='center', fontsize=10, fontweight='bold', color='#7f8c8d')
        
        # 2. Step Title (y = 3.02)
        ax.text(x_pos + box_width/2, y_pos + 1.02, step['title'], 
                ha='center', va='center', fontsize=11.5, fontweight='bold', color='#2c3e50')
                
        # 3. Actor (y = 0.78)
        ax.text(x_pos + box_width/2, y_pos + 0.78, f"By: {step['actor']}", 
                ha='center', va='center', fontsize=9.5, fontweight='bold', color='#34495e')
                
        # 4. Time (y = 0.54)
        time_color = '#c0392b' if step["bottleneck"] else '#27ae60'
        ax.text(x_pos + box_width/2, y_pos + 0.54, f"Time: {step['time']}", 
                ha='center', va='center', fontsize=9, color=time_color, fontweight='bold')
                
        # 5. Tag (y = 0.34) - only if not empty
        if step.get("tag"):
            ax.text(x_pos + box_width/2, y_pos + 0.34, step["tag"], 
                    ha='center', va='center', fontsize=8, color='#c0392b', fontweight='bold')
                
        # 6. Description (y = 0.15)
        ax.text(x_pos + box_width/2, y_pos + 0.14, step['desc'], 
                ha='center', va='center', fontsize=8, style='italic', color='#7f8c8d')
                
        # Draw arrow to the next box
        if i < len(steps) - 1:
            arrow_start_x = x_pos + box_width + 0.08
            arrow_end_x = x_pos + 2.65 - 0.08
            ax.annotate('', xy=(arrow_end_x, y_pos + box_height/2), 
                        xytext=(arrow_start_x, y_pos + box_height/2),
                        arrowprops=dict(arrowstyle="-|>", color='#34495e', lw=2, mutation_scale=15))

    # Overall Stats / Legend at the bottom
    ax.text(0.3, 1.6, "[BOTTLENECK]: Causes operational delays  |  [HANDOFF]: Handoff point between departments",
            fontsize=9.5, color='#7f8c8d')
    ax.text(11.5, 1.6, "Total Lead Time: 13 mins",
            ha='right', fontsize=11, fontweight='bold', color='#2c3e50')

    # Set boundaries and title
    ax.set_xlim(0, 13.5)
    ax.set_ylim(1.4, 4.0)
    ax.axis('off')

    plt.title("VINHOMES RESIDENT FEEDBACK - CURRENT-STATE WORKFLOW\n(Manual process before AI implementation)", 
              fontsize=14, fontweight='bold', pad=25, color='#2c3e50')

    # Save to PDF file
    output_path = os.path.join("ai-product-lab-hihi", "04-workflow-diagram.pdf")
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches='tight')
    print(f"Successfully generated workflow diagram at {output_path}")

if __name__ == "__main__":
    draw_workflow()
