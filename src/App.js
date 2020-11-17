import React from 'react';
//import logo from './logo.svg';
import './App.css';
import Form from './Form';

class App extends React.Component {
    render(){
		return (
			<div className="App">
				<header className="App-header">
					<Form />
				</header>
			</div>
		);
    }
}

export default App;
