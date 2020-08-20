import React from 'react';
// import { Router } from 'react-router-dom';

class Signup extends React.Component{
  render(){
    return (
    <form>
      <h3>Sign Up</h3>

      <label>Я являюсь:</label>

        
          <input type="radio" name="role" value="student"/>
          <label>Учеником</label>

          <input type="radio" name="role" value="tutor" />
          <label>Репетитором</label>

      <div>
          <label>E-mail</label>
          <input type="email"/>
      </div>

      <div>
          <label>Фамилия</label>
          <input type="text"/>
      </div>

      <div>
          <label>Имя</label>
          <input type="text"/>
      </div>

      <div>
          <label>Пароль</label>
          <input type="password"/>
      </div>

      <div>
          <label>Подтверждение пароля</label>
          <input type="password"/>
      </div>

      <button type="submit">Sign Up</button>

      <p>
          Уже есть учетная запись?<a href="/">Вход</a>
      </p>
  </form>
    );
  }
}

export default Signup;
