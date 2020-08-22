import React from 'react';

import { loadStudentInfo } from '../api/backend';

const EduLevel = {
    toInternal: {
        Low: "1",
        Middle: "2",
        High: "3",
    },
    toExternal: {
        1: "Low",
        2: "Middle",
        3: "High",
    },
};

class Info extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            userId: props.userId,
            eduLevel: "",
        }
    }

    updateInfo = (data, status = 200) => {
        if (status === 200) {
            this.setState({
                eduLevel: data.edu_level,
            })
        }
        else {
            console.log("There was an error")
        }
    }

    componentDidMount() {
        const userId = this.state.userId
        loadStudentInfo(userId, this.updateInfo)
    }

    render() {
        return (
            <div>
                <h2>Student info </h2>
                <p>Education Level: {EduLevel.toExternal[this.state.eduLevel]}</p>
            </div>
        );
    }
}

export default Info;
