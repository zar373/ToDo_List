from selenium import webdriver
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the todo list webpage


# Find the input field for adding a new item
input_field = driver.find_element_by_id("card-{{i.id}}")

# Type the new task in the input field
input_field.send_keys("New Task")

# Find the submit button and click it
submit_button = driver.find_element_by_id("submit-{{i.id}}")
submit_button.click()

# Allow some time for the task to be added (you might need to wait for AJAX or page load)


# Check if the new task is present in the list
new_task_element = driver.find_element_by_xpath("//div[@id='card-{{i.id}}']")
assert new_task_element is not None, "New task not found in the list"

# Close the browser
driver.quit()
