//CSRF_TOKEN starts
function getCSRFToken() {
  let csrfToken = null;
  const cookies = document.cookie.split(";");
  for (let cookie of cookies) {
    const cookiePair = cookie.trim().split("=");
    if (cookiePair[0] === "csrftoken") {
      csrfToken = cookiePair[1];
    }
  }
  return csrfToken;
}

function getCSRFToken() {
  return document.querySelector("[name=csrfmiddlewaretoken]").value;
}
//CSRF_TOKEN ENds

//Creating Employees starts
function createEmployee() {
  const data = {
    name: document.getElementById("name").value.trim(),
    email: document.getElementById("email").value.trim(),
    age: document.getElementById("age").value.trim(),
    gender: document.getElementById("gender").value.trim(),
    phoneNo: document.getElementById("phoneNo").value.trim(),
    hno: document.getElementById("hno").value.trim(),
    street: document.getElementById("street").value.trim(),
    city: document.getElementById("city").value.trim(),
    state: document.getElementById("state").value.trim(),
    companyName: document.getElementById("companyName").value.trim(),
    fromDate: document.getElementById("fromDate").value.trim(),
    toDate: document.getElementById("toDate").value.trim(),
    address: document.getElementById("address").value.trim(),
    qualificationName: document.getElementById("qualificationName").value.trim(),
    percentage: document.getElementById("percentage").value.trim(),
    title: document.getElementById("title").value.trim(),
    description: document.getElementById("description").value.trim(),
    photo: document.getElementById("photo").files[0],
  };

  const formData = new FormData();
  for (const key in data) {
    formData.append(key, data[key]);
  }

  $.ajax({
    url: "/create/",
    method: "POST",
    data: formData,
    contentType: false, // Important for file uploads
    processData: false, // Important for file uploads
    headers: {
      "X-CSRFToken": getCSRFToken(),
    },
    success: function (response) {
      alert(response.message);
      $("#employeeModal").modal("hide");
      console.log("Employee created, reloading employee list");
      loadEmployeeList(); // Reload the list after creation
    },
    error: function (error) {
      alert(error.responseJSON.error);
    },
  });
}
//Creating Employees Ends


//To view data in template starts
// $(document).ready(function () {
//   // Call the function to load employees on page load
//   loadEmployeeList();
// });

// Move this function outside to the global scope
function loadEmployeeList() {
  $.ajax({
    url: "/List/", // Adjust the URL to match your Django view's URL
    method: "GET",
    headers: {
      "X-Requested-With": "XMLHttpRequest", // Indicate it's an AJAX request
    },
    success: function (data) {
      populateEmployeeTable(data); // Call function to populate the table
    },
    error: function (xhr) {
      alert("Error fetching employee data: " + xhr.responseText);
    },
  });
}

function populateEmployeeTable(employees) {
  const employeeTable = $("#employeeTable"); // Get the table body element
  employeeTable.empty(); // Clear the existing table data

  if (employees.length > 0) {
    employees.forEach(function (employee) {
      const row = `<tr>
                            <td>${employee.name}</td>
                            <td>${employee.email}</td>
                            <td>${employee.age}</td>
                            <td>${employee.gender}</td>
                            <td>
                                <button class="btn btn-warning" data-bs-toggle="modal" data-bs-target="#employeeModal2" onclick="editEmployee(${employee.id})">Edit</button>
                                <button class="btn btn-danger" onclick="deleteEmployee(${employee.id})">Delete</button>
                            </td>
                        </tr>`;
      employeeTable.append(row); // Append the new row to the table
    });
  } else {
    employeeTable.append('<tr><td colspan="5">No employees found</td></tr>');
  }
}
//To view data in template ends

//To delete data starts
function deleteEmployee(employeeId) {
  if (confirm("Are you sure you want to delete this employee?")) {
    // Send AJAX DELETE request
    fetch(`/delete_employee_url/${employeeId}/`, {
      method: "DELETE",
      headers: {
        "X-CSRFToken": "{{ csrf_token }}", // Ensure the CSRF token is passed
      },
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.message) {
          alert(data.message); // Show success message
          location.reload(); // Reload the page to update the employee list
        } else if (data.error) {
          alert(data.error); // Show error message
        }
      })
      .catch((error) => console.error("Error:", error));
  }
}
//to delete data ends


function editEmployee(employeeId) {
    $.ajax({
        url: '/edit-employee/' + employeeId + '/',  // Ensure this matches your URL pattern
        method: 'GET',
        success: function(data) {
            // Populate the form fields with the employee data
            $('#employeeId').val(employeeId);
            $('#editName').val(data.name);
            $('#editEmail').val(data.email);
            $('#editAge').val(data.age);
            $('#editGender').val(data.gender);
            $('#editPhoneNo').val(data.phoneNo);
            $('#editHno').val(data.hno);
            $('#editStreet').val(data.street);
            $('#editCity').val(data.city);
            $('#editState').val(data.state);
            $('#editCompanyName').val(data.companyName);
            $('#editFromDate').val(data.fromDate);
            $('#editToDate').val(data.toDate);
            $('#editAddress').val(data.address);
            $('#editQualificationName').val(data.qualificationName);
            $('#editPercentage').val(data.percentage);
            $('#editTitle').val(data.title);
            $('#editDescription').val(data.description);
            // $('#editPhoto').val(data.photo);
            if (data.photo) {
                $('#currentPhoto').text('Current photo: ' + data.photo);
            } else {
                $('#currentPhoto').text('No photo uploaded.');
            }
            $('#employeeModal2').modal('show');
        },
        error: function(xhr, status, error) {
            console.log("Error fetching employee data:", xhr.responseText);
            alert("Error fetching employee data.");
        }
    });
}
function updateEmployee() {
  var formData = new FormData(document.getElementById('editEmployeeForm'));  // Use vanilla JS to get the form data
  var employeeId = document.getElementById('employeeId').value;  // Get the employee ID
  
  // Perform the AJAX request using jQuery
  $.ajax({
      url: '/edit-employee/' + employeeId + '/',  // Adjust the URL to your endpoint
      method: 'POST',
      data: formData,
      processData: false,
      contentType: false,
      success: function(response) {
          alert(response.message);
          location.reload();  // Reload the page to see the updated data
      },
      error: function(xhr) {
          alert('Error: ' + xhr.responseJSON.error);
      }
  });
}

// Attach event listener to the modal open event
$('#employeeModal2').on('show.bs.modal', function(event) {
  var button = $(event.relatedTarget); // Button that triggered the modal
  var employeeId = button.data('employee-id'); // Extract employee ID from data-* attribute
  fetchEmployeeData(employeeId); // Fetch and populate the employee data
});

// $('#updateEmployeeBtn').click(function() {
//     var formData = new FormData($('#editEmployeeForm')[0]);
//     $.ajax({
//         url: '/edit-employee' + $('#employeeId').val() + '/',  // Adjust the URL to your endpoint
//         method: 'POST',
//         data: formData,
//         processData: false,
//         contentType: false,
//         success: function(response) {
//             alert(response.message);
//             location.reload();  // Reload the page to see the updated data
//         },
//         error: function(xhr) {
//             alert('Error: ' + xhr.responseJSON.error);
//         }
//     });
// });

// // Attach event listener to the modal open event
// $('#employeeModal2').on('show.bs.modal', function(event) {
//     var button = $(event.relatedTarget); // Button that triggered the modal
//     var employeeId = button.data('employee-id'); // Extract employee ID from data-* attribute
//     fetchEmployeeData(employeeId); // Fetch and populate the employee data

//     // Add the employeeId to the Update button click event
//     $('#updateEmployeeBtn').off('click').on('click', function() {
//         updateEmployee(employeeId); // Call updateEmployee with the employeeId
//     });
// });
