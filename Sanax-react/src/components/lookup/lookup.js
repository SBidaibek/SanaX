function lookup(method, endpoint, callback, data) {
    let jsonData;
    if (data) {
        jsonData = JSON.stringify(data)
    }
    const xhr = new XMLHttpRequest()
    const url = `http://127.0.0.1:8000${endpoint}`

    xhr.responseType = "json"
    xhr.open(method, url)
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.onload = () => {
        callback(xhr.response, xhr.status)
    }
    xhr.onerror = (e) => {
        console.log(e)
        callback({ "message": "Error request" }, 400)
    }
    xhr.send(jsonData)
}

export function loadStudentInfo(userId, callback) {
    lookup("POST", `/api/get_student_info/`, callback, { "id": userId })
}

export function loadStudentCourseList(userId, callback) {
    lookup("POST", `/api/get_student_course_list/`, callback, { "id": userId })
}

export function loadStudentChoiceList(userId, callback) {
    lookup("POST", `/api/get_student_choice_list/`, callback, { "id": userId })
}