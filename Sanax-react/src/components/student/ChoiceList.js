import React from 'react';

import { loadStudentChoiceList } from '../lookup/lookup';
import Choice from './Choice';

class ChoiceList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            userId: props.userId,
            choiceList: [],
        }
    }

    updateList = (data, status = 200) => {
        if (status === 200) {
            this.setState({
                choiceList: data,
            })
        }
        else {
            console.log("There was an error")
        }
    }

    componentDidMount() {
        const userId = this.state.userId
        loadStudentChoiceList(userId, this.updateList)
    }

    render() {
        return (
            <div>
                <h2>Choice List: </h2>
                <ul>
                    {this.state.choiceList.map((item, index) => {
                        return <li key={item.id}>
                            <Choice choiceData={item} />
                        </li>
                    })}
                </ul>
            </div>
        );
    }
}

export default ChoiceList;
