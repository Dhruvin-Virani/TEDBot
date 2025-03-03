# import requests
# from bs4 import BeautifulSoup

# # Step 4: Make an HTTP Request
# url = 'https://kpgu.ac.in/' 
# response = requests.get(url)

# soup = BeautifulSoup(response.text, 'html.parser')

# course_data = []

# # Find the HTML elements that contain course information
# course_elements = soup.find_all('div', class_='course-info')

# for course in course_elements:
#     # Extract course details
#     course_name = course.find('h2').text
#     course_description = course.find('p').text

#     course_data.append({
#         'Course Name': course_name,
#         'Description': course_description,
#     })

# import csv

# with open('course_data.csv', 'w', newline='') as csvfile:
#     fieldnames = ['Course Name', 'Description']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     for course in course_data:
#         writer.writerow(course)

# print("Data successfully scraped and saved to course_data.csv.")


import requests
from bs4 import BeautifulSoup

# Step 1: Make an HTTP request to the URL
url = 'https://kpgu.ac.in/'  # Replace with the specific webpage URL
response = requests.get(url)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract data
# Identify specific HTML elements containing the data you need
# For example, if you want to scrape links, you might use:
links = [a['href'] for a in soup.find_all('a')]
count = 0
# Print or process the extracted data
for link in links:
    count = count + 1
    print(link)

print(count)
