// client/src/Demo.js
//import React, {useState, useEffect} from 'react';
import React from 'react';
//import flask from 'flask-urls.macro';
//const formURL = flask`form`;
const formfullURL = "/api/form";
export default class Form extends React.Component {
    constructor(props) {
        super(props);

        // Este enlace es necesario para hacer que `this` funcione en el callback
        this.fieldChanged = this.fieldChanged.bind(this);
        this.setYesers = this.setYesers.bind(this);
        this.reflectPrediction = this.reflectPrediction.bind(this);
        this.state = {job: 'admin.', marital: 'married', education: 'unknown', contact: 'unknown',
        day: 1, month: 'jan', poutcome: 'unknown', likely: 0, duration: '', default: "no", balance:'',
        housing: "false", loan: "false", campaign: '', 'pdays': '', 'previous': '', age:''};
        //new data: {'age': 42, 'job': 5, 'marital': 1, 'education': 3, 'default': 1, 'balance': 2, 'housing': 1, 'loan': 0, 'contact': 0, 'day': 5, 'month': 4, 'duration': 380, 'campaign': 1, 'pdays': -1, 'previous': 0, 'poutcome': 0}
    }
    setYesers (e){
       //This function sets the fields to values that give positive for the client engagement prediction 
        var stateobj = {job: 'admin.', marital: 'married', education: 'secondary', contact: 'unknown',
        day: 5, month: 'may', poutcome: 'unknown', likely: 0, duration: '1042', default: "no", balance:'2343',
        housing: "yes", loan: "no", campaign: 1, 'pdays': '-1', 'previous': '0', age: '59'};
        this.setState(stateobj);
        //console.log(newstate);
        var formdat = new FormData();
        var entries = Object.entries(stateobj);
        for (const [name, value] of entries) {
            formdat.append(name, value);
        }
        //document.getElementById("submitter").style['background-color'] = 'yellow';
        var that = this;
        fetch(formfullURL, {'mode':'cors', 'method': 'post', 'body': formdat})
        .then(function (response){
            return response.json();
        })
        .then(that.reflectPrediction)
    }
    reflectPrediction (myjson){
        var likely;
        if (myjson.status === 'ok'){
            likely = myjson.prediction;
            console.log("likely: "+likely);
        } else {
            likely = 0;
            console.log("likely: 0 because lacking data");
        };
        if (likely){
            document.getElementById("submitter").style['background-color'] = '#02ed39';
        } else {
            document.getElementById("submitter").style['background-color'] = '#ed3902';
        }
        this.setState({likely: likely});
    }
    fieldChanged (e){
        var stateobj = {[e.target.name]: e.target.value};
        this.setState(stateobj);
        var newstate = this.state || {};
        newstate[e.target.name] = e.target.value; //updates the stat with its newast value if the state object has not been updated
        var formdat = new FormData();
        var entries = Object.entries(newstate);
        for (const [name, value] of entries) {
            formdat.append(name, value);
        }
        document.getElementById("submitter").style['background-color'] = 'yellow';
        var that = this;
        fetch(formfullURL, {'mode':'cors', 'method': 'post', 'body': formdat})
        .then(function (response){
            return response.json();
        })
        .then(that.reflectPrediction)
    }
    render(){
        return(
        <table>
        <tbody>
          <tr><td><label htmlFor="age">Age</label></td>
          <td><input id="age" name="age" value={this.state.age} onChange={this.fieldChanged} type="text"/>
          </td>
          <td><label htmlFor="job">Type of job</label></td>
          <td><select id="job" name="job" value={this.state.job} onChange={this.fieldChanged}><option value="admin.">admin.</option><option value="unknown">unknown</option><option value="unemployed">unemployed</option><option value="management">management</option><option value="housemaid">housemaid</option><option value="entrepreneur">entrepreneur</option><option value="student">student</option><option value="blue-collar">blue-collar</option><option value="self-employed">self-employed</option><option value="retired">retired</option><option value="technician">technician</option><option value="services">services</option></select>
          </td></tr>

          <tr><td><label htmlFor="marital">Marital status</label></td>
          <td><select id="marital" name="marital" value={this.state.marital} onChange={this.fieldChanged}><option value="married">married</option><option value="divorced">divorced</option><option value="single">single</option></select>
          </td><td><label htmlFor="education">Education</label></td>
          <td><select id="education" name="education" value={this.state.education} onChange={this.fieldChanged}><option value="unknown">unknown</option><option value="secondary">secondary</option><option value="primary">primary</option><option value="tertiary">tertiary</option></select>
          </td></tr>

          <tr><td><label htmlFor="default">Has credit in default?</label></td>
          <td><input id="default" name="default" value={this.state.default} onChange={this.fieldChanged} type="checkbox"/>
          </td><td><label htmlFor="balance">Average year balance, in euros</label></td>
          <td><input id="balance" name="balance" value={this.state.balance} onChange={this.fieldChanged} type="text"/>
          </td></tr>

          <tr><td><label htmlFor="housing">Has housing loan?</label></td>
          <td><input id="housing" name="housing" value={this.state.housing} onChange={this.fieldChanged} type="checkbox"/>
          </td><td><label htmlFor="loan">Has personal loan?</label></td>
          <td><input id="loan" name="loan" value={this.state.loan} onChange={this.fieldChanged} type="checkbox"/>
          </td></tr>

          <tr><td><label htmlFor="contact">Contact communication type</label></td>
          <td><select id="contact" name="contact" value={this.state.contact} onChange={this.fieldChanged}><option value="unknown">unknown</option><option value="telephone">telephone</option><option value="cellular">cellular</option></select>
          </td></tr>
          <tr><td><label htmlFor="day">Last contact day of the month</label></td>
          <td><input id="day" name="day" value={this.state.day} onChange={this.fieldChanged} type="text"/>
          </td>
          <td><label htmlFor="month">Last contact month</label></td>
          <td><select id="month" name="month" value={this.state.month} onChange={this.fieldChanged}><option value="jan">January</option>
          <option value="feb">February</option><option value="mar">March</option><option value="apr">April</option>
          <option value="may">May</option><option value="jun">June</option><option value="jul">July</option><option value="aug">
          August</option><option value="sep">September</option><option value="oct">
          October</option><option value="nov">November</option><option value="dec">December</option></select>
          </td></tr>

          <tr><td><label htmlFor="duration">Last contact duration, in seconds (numeric)</label></td>
          <td><input id="duration" name="duration"  value={this.state.duration} onChange={this.fieldChanged} type="text"/>
          </td><td><label htmlFor="campaign"># of contacts performed during this campaign</label></td>
          <td><input id="campaign" name="campaign" value={this.state.campaign} onChange={this.fieldChanged} type="text"/>
          </td></tr>

          <tr><td><label htmlFor="pdays"># days passed by after the client was last contacted from a previous campaign</label></td>
          <td><input id="pdays" name="pdays" value={this.state.pdays} onChange={this.fieldChanged} type="text"/>
          </td><td><label htmlFor="previous"># of contacts performed before this campaign</label></td>
          <td><input id="previous" name="previous" value={this.state.previous} onChange={this.fieldChanged} type="text"/>
          </td></tr>

          <tr><td><label htmlFor="poutcome">Previous marketing campaign outcome</label></td>
          <td><select id="poutcome" name="poutcome" value={this.state.poutcome} onChange={this.fieldChanged}><option value="unknown">unknown</option><option value="other">other</option><option value="failure">failure</option><option value="success">success</option></select>
          </td></tr>
          <tr><td><input type="button" onClick={this.setYesers} value="Positive example"/></td>
          <td><input type="submit" id="submitter" name="submitter" disabled={!this.state.likely}/></td></tr>
              
        </tbody>
        </table>
        );
    }
}
