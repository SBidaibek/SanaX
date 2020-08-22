import React from 'react';

import { createChoice } from '../../api/backend'


class Signup extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            data: {
                id: props.userId,
                subject: null,
                language: null,
                difficulty: null,
                preferredLowestPrice: null,
                preferredHighestPrice: null,
                preferPersonalLessons: null,
                preferredDuration: null,
            },
        }
    }

    submitCallback = (data, status) => {
        console.log(data)
    }

    handleSubmit = (event) => {
        event.preventDefault()
        createChoice(this.state.data, this.submitCallback)
    }

    handleChange = (event) => {
        const target = event.target
        const name = target.name
        const value = (target.type === "checkbox" ? target.checked : target.value)
        this.setState((state) => {
            var newData = state.data
            newData[name] = value
            return { data: newData }
        })
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit} onChange={this.handleChange}>
                <h2>Create Choice</h2>

                <div>
                    <label>Subject:</label>

                    <input type="radio" name="subject" value="1" />
                    <label>Mathematics</label>
                </div>

                <div>
                    <label>Language:</label>

                    <input type="radio" name="language" value="1" />
                    <label>Russian</label>

                    <input type="radio" name="language" value="2" />
                    <label>Kazakh</label>

                    <input type="radio" name="language" value="3" />
                    <label>English</label>
                </div>

                <div>
                    <label>Difficulty</label>
                    <input type="number" name="difficulty" />
                </div>

                <div>
                    <label>Price Range</label>
                    <input type="number" name="preferredLowestPrice" />
                    <input type="number" name="preferredHighestPrice" />
                </div>

                <div>
                    <input type="checkbox" name="preferPersonalLessons" />
                    <label>Personal lessons preferred</label>
                </div>

                <div>
                    <label>Duration</label>
                    <input type="time" name="preferredDuration" />
                </div>

                <button type="submit">Submit</button>
            </form>
        );
    }
}

export default Signup;
