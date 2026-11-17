import React from 'react';

export default class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.error('SpendWise UI Error Boundary caught an error:', error, errorInfo);
  }

  handleReset = () => {
    try {
      localStorage.removeItem('spendwise-token');
      localStorage.removeItem('spendwise-user');
      localStorage.removeItem('spendwise-theme');
      localStorage.removeItem('ledgerly-token');
      localStorage.removeItem('ledgerly-user');
      localStorage.removeItem('ledgerly-theme');
    } catch (e) {
      console.error('Error clearing storage:', e);
    }
    window.location.href = '/login';
  };

  render() {
    if (this.state.hasError) {
      return (
        <div style={{
          minHeight: '100vh',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          backgroundColor: '#F7F5F0',
          color: '#1B1F23',
          fontFamily: 'Inter, system-ui, sans-serif',
          padding: '24px',
          textAlign: 'center',
        }}>
          <div style={{
            maxWidth: '480px',
            backgroundColor: '#ffffff',
            padding: '32px',
            borderRadius: '12px',
            boxShadow: '0 4px 16px rgba(0,0,0,0.08)',
            border: '1px solid #E4E0D6'
          }}>
            <h2 style={{ fontSize: '20px', fontWeight: 'bold', marginBottom: '12px', color: '#2F6F4E' }}>
              SpendWise Application Recovery
            </h2>
            <p style={{ fontSize: '14px', color: '#6E6759', marginBottom: '20px', lineHeight: '1.5' }}>
              An unexpected display issue occurred. Clicking the button below will clear any corrupted local session data and reload the sign-in screen cleanly.
            </p>
            <button
              onClick={this.handleReset}
              style={{
                backgroundColor: '#2F6F4E',
                color: '#ffffff',
                border: 'none',
                padding: '10px 20px',
                borderRadius: '8px',
                fontWeight: '600',
                fontSize: '14px',
                cursor: 'pointer'
              }}
            >
              Reset Session & Reload
            </button>
          </div>
        </div>
      );
    }
    return this.props.children;
  }
}
