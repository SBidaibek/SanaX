import React from 'react';

import Info from './Info';
import CourseList from './CourseList';
import ChoiceList from './ChoiceList';


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

                <CourseList userId={this.state.userId} />

                <ChoiceList userId={this.state.userId} />
            </div>
        );
    }
}

export default Index;
