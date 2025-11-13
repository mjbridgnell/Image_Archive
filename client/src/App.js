import React, { useState, useEffect } from 'react';
import { Display_Images } from './ImageList';
import LoginForm from "./LoginForm";

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
      fetch("/auth/whoami", {
        credentials: "include"
      })
        .then((res) => (res.ok ? res.json() : null))
        .then((data) => {
          if (data?.user) setUser(data.user);
        });
  }, []);

  if (!user) {
    return <LoginForm onLoginSuccess={setUser} />;
  }
  return <Display_Images onLogout={() => setUser(null)} />;

}    

export default App