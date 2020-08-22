import React from 'react';


const Subject = {
    toInternal: {
        Mathematics: "1",
    },
    toExternal: {
        1: "Mathematics",
    },
};

const Language = {
    toInternal: {
        Russian: "1",
        Kazakh: "2",
        English: "3",
    },
    toExternal: {
        1: "Russian",
        2: "Kazakh",
        3: "English",
    },
};

class Choice extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            id: props.choiceData.id,
            subject: props.choiceData.subject,
            language: props.choiceData.language,
        }
    }

    render() {
        return (
            <div>
                <p>On choice {this.state.id} you chose {Subject.toExternal[this.state.subject]} in {Language.toExternal[this.state.language]}</p>
            </div>
        );
    }
}

export default Choice;
