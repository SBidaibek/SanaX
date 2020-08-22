import React from 'react';

import Info from './Info';
import CourseList from './CourseList';
import ChoiceList from './Choice/List';
import ChoiceForm from './Choice/Form';


class Index extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            userId: props.match.params.userId,
        }
    }

    render() {
        return (
            <div>
                <Info userId={this.state.userId} />
                <br />

                <ChoiceForm userId={this.state.userId} />
                <br />

                <CourseList userId={this.state.userId} />
                <br />

                <ChoiceList userId={this.state.userId} />
                <br />
            </div>
        );
    }
}

export default Index;
