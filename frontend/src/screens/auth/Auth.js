import React, { useState } from 'react'

// components
import SignIn from './SignIn'
import SignUp from './SignUp'

const Auth = ({ token }) => {
  const [activeView, setActiveView] = useState('signin')
  return (
    <>
      {activeView === 'signup' && (
        <div className='w-full flex flex-col'>
          <SignUp viewHandler={() => setActiveView('signin')} />
        </div>
      )}
      {activeView === 'signin' && (
        <div className='w-full flex flex-col'>
          <SignIn viewHandler={() => setActiveView('signup')} />
        </div>
      )}
    </>
  )
}

export default Auth
