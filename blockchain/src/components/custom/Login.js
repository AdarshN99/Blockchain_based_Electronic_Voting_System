import React, { Component } from 'react';

class Login extends Component {

    constructor(props){
        super(props);
        this.state = {
            username: '',
            password: ''
        };
    }

    handleInputChange = (e) => {
        this.setState({
            [e.target.name]: e.target.value,
        });
    }

    handleSubmit = (e) => {
        e.preventDefault();
        const { username, password } = this.state;

        // Hardcoded check (this is insecure and just for demonstration purposes)
        const hardcodedUsername = 'admin';
        const hardcodedPassword = 'admin123'; // In real-world apps, never do this

        if (username === hardcodedUsername && password === hardcodedPassword) {
            // If credentials match, redirect to /newelection
            window.location.assign("/newelection");
        } else {
            // If credentials don't match, alert the user
            alert('Incorrect Username or Password');
        }
    }

    render(){
        return(
            <div className="container">
                <form onSubmit={this.handleSubmit}>
                    <input type="text" id="username" name="username" onChange={this.handleInputChange} required/>
                    <label htmlFor="username">Username</label><br/>
                    <input type="password" id="password" name="password" onChange={this.handleInputChange} required/>
                    <label htmlFor="password">Password</label><br/><br/>
                    <button className="btn blue darken-2" type="submit" name="action">Submit
                        <i className="material-icons right">send</i>
                    </button>
                </form>
            </div>      
        );
    }
}

export default Login;