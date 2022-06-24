import cx from 'classnames';
import { Component } from 'react';

export default class Counter extends Component {
    constructor(props) {
        super(props);
    
        this.state = {
            counter: 42
        };
    
    
        this.onClick = this.onClick.bind(this);
    }

    onClick(e)
    {
        this.setState({ counter: this.state.counter + 1 });
    }

    render() {
        const { counter } = this.state;

        return (
            <>
                <div>
                    <h2>{counter}</h2>
                </div>
                <style>{`
                    .counter-button {
                        font-size: 1rem;
                        padding: 5px 10px;
                        color:  #585858;
                    }
                `}</style>
                <button className={"counter-button"} onClick={this.onClick}>Click</button>
            </>
        );
    }
}


