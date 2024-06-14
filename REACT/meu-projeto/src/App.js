import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Olá mundo e React !</h1>
        <p>Começando meu projeto</p>
        <img src={logo} className="App-logo" alt="logo" />
        <p>
         Criado por Luis Carlos de Queiroz
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
