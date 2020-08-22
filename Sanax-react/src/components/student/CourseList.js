import React from 'react';

import { loadStudentCourseList } from '../lookup/lookup';

class CourseList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            userId: props.userId,
            courseList: [],
        }
    }

    updateList = (data, status = 200) => {
        if (status === 200) {
            this.setState({
                courseList: data,
            })
        }
        else {
            console.log("There was an error")
        }
    }

    componentDidMount() {
        const userId = this.state.userId
        loadStudentCourseList(userId, this.updateList)
    }

    render() {
        return (
            <div>
                <h2>Course List: </h2>
                <ul>
                    {this.state.courseList.map((item, index) => {
                        return <li key={item.id}>
                            {index + 1}. {item.name} - {item.description} - {item.progress}
                        </li>
                    })}
                </ul>
            </div>
        );
    }
}

export default CourseList;
