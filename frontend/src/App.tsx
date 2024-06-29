import React, { useState } from 'react';
import SignIn from './components/SignIn';
import LogIn from './components/LogIn';

const App: React.FC = () => {
  const [view, setView] = useState<'signIn' | 'logIn'>('signIn');

  return (
    <div className="App">
      <header>
        <h1 style={{ color: "black" }}>MyCompta Application</h1>
        <nav>
          <button onClick={() => setView('signIn')}>Sign In</button>
          <button onClick={() => setView('logIn')}>Log In</button>
        </nav>
      </header>
      <main>
        {view === 'signIn' && <SignIn />}
        {view === 'logIn' && <LogIn />}
      </main>
    </div>
  );
};

export default App;
