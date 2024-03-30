import yaml

def convert_to_coco_yaml(txt_content):
    coco_data = {'train': './train/images', 'val': './val/images', 'nc': 0, 'names': []}
    
    lines = txt_content.splitlines()
    i = 0
    while i < len(lines):
        image_path = lines[i].strip()
        num_bounding_boxes = int(lines[i + 1].strip())
        
        # Update 'nc' and 'names' based on the class information
        for j in range(i + 2, i + 2 + num_bounding_boxes):
            class_id = int(lines[j].split()[5])  # Assuming the class information is at index 5
            if class_id not in coco_data['names']:
                coco_data['names'].append(class_id)
        
        i += 2 + num_bounding_boxes
        
    coco_data['nc'] = len(coco_data['names'])
    
    return coco_data

# Example input
ground_truth_txt = """0--Parade/0_Parade_marchingband_1_849.jpg
1
449 330 122 149 0 0 0 0 0 0 
0--Parade/0_Parade_Parade_0_904.jpg
1
361 98 263 339 0 0 0 0 0 0
0--Parade/0_Parade_marchingband_1_799.jpg
21
78 221 7 8 2 0 0 0 0 0 
78 238 14 17 2 0 0 0 0 0 
113 212 11 15 2 0 0 0 0 0 
134 260 15 15 2 0 0 0 0 0 
163 250 14 17 2 0 0 0 0 0 
201 218 10 12 2 0 0 0 0 0 
182 266 15 17 2 0 0 0 0 0 
245 279 18 15 2 0 0 0 0 0 
304 265 16 17 2 0 0 0 2 1 
328 295 16 20 2 0 0 0 0 0 
389 281 17 19 2 0 0 0 2 0 
406 293 21 21 2 0 1 0 0 0 
436 290 22 17 2 0 0 0 0 0 
522 328 21 18 2 0 1 0 0 0 
643 320 23 22 2 0 0 0 0 0 
653 224 17 25 2 0 0 0 0 0 
793 337 23 30 2 0 0 0 0 0 
535 311 16 17 2 0 0 0 1 0 
29 220 11 15 2 0 0 0 0 0 
3 232 11 15 2 0 0 0 2 0 
20 215 12 16 2 0 0 0 2 0
"""

# Convert to COCO YAML format
coco_yaml_data = convert_to_coco_yaml(ground_truth_txt)

# Print or save the resulting COCO YAML data
with open('output.yaml', 'w') as yaml_file:
    yaml.dump(coco_yaml_data, yaml_file, default_flow_style=False)

print(coco_yaml_data)
