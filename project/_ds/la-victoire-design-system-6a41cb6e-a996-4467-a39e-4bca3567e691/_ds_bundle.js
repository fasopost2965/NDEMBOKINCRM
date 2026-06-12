/* @ds-bundle: {"format":3,"namespace":"LaVictoireDesignSystem_6a41cb","components":[{"name":"Avatar","sourcePath":"components/core/Avatar.jsx"},{"name":"Badge","sourcePath":"components/core/Badge.jsx"},{"name":"Button","sourcePath":"components/core/Button.jsx"},{"name":"Card","sourcePath":"components/core/Card.jsx"},{"name":"Divider","sourcePath":"components/core/Divider.jsx"},{"name":"Input","sourcePath":"components/core/Input.jsx"}],"sourceHashes":{"components/core/Avatar.jsx":"98669c2c8e7f","components/core/Badge.jsx":"4a7a55443289","components/core/Button.jsx":"673b0dbb9bda","components/core/Card.jsx":"5124128017d3","components/core/Divider.jsx":"45ef36cef1e5","components/core/Input.jsx":"f5bf7a163be5"},"inlinedExternals":[],"unexposedExports":[]} */

(() => {

const __ds_ns = (window.LaVictoireDesignSystem_6a41cb = window.LaVictoireDesignSystem_6a41cb || {});

const __ds_scope = {};

(__ds_ns.__errors = __ds_ns.__errors || []);

// components/core/Avatar.jsx
try { (() => {
function Avatar(props) {
  const {
    src,
    alt = '',
    name,
    size = 'md',
    ...rest
  } = props;
  const sizeMap = {
    sm: 32,
    md: 40,
    lg: 56,
    xl: 72
  };
  const px = sizeMap[size] || 40;
  const getInitials = n => {
    if (!n) return '?';
    const parts = n.trim().split(/\s+/);
    if (parts.length >= 2) return (parts[0][0] + parts[parts.length - 1][0]).toUpperCase();
    return parts[0][0].toUpperCase();
  };
  const containerStyle = {
    width: px,
    height: px,
    borderRadius: 'var(--radius-full)',
    overflow: 'hidden',
    display: 'inline-flex',
    alignItems: 'center',
    justifyContent: 'center',
    flexShrink: 0,
    background: src ? 'var(--neutral-200)' : 'var(--navy-600)',
    color: 'var(--gold-300)',
    fontFamily: 'var(--font-display)',
    fontWeight: 'var(--weight-semibold)',
    fontSize: px * 0.4,
    lineHeight: 1,
    letterSpacing: 'var(--tracking-wide)',
    border: '2px solid var(--border-gold-muted)'
  };
  const imgStyle = {
    width: '100%',
    height: '100%',
    objectFit: 'cover'
  };
  if (src) {
    return React.createElement('div', {
      style: containerStyle,
      ...rest
    }, React.createElement('img', {
      src,
      alt: alt || name || '',
      style: imgStyle
    }));
  }
  return React.createElement('div', {
    style: containerStyle,
    ...rest
  }, getInitials(name));
}
Object.assign(__ds_scope, { Avatar });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Avatar.jsx", error: String((e && e.message) || e) }); }

// components/core/Badge.jsx
try { (() => {
function Badge(props) {
  const {
    children,
    variant = 'default',
    size = 'md',
    ...rest
  } = props;
  const variantStyles = {
    default: {
      background: 'var(--neutral-100)',
      color: 'var(--text-secondary)',
      border: '1px solid var(--border-default)'
    },
    gold: {
      background: 'var(--gold-50)',
      color: 'var(--gold-700)',
      border: '1px solid var(--gold-200)'
    },
    navy: {
      background: 'var(--navy-600)',
      color: 'var(--neutral-100)',
      border: '1px solid var(--navy-500)'
    },
    success: {
      background: '#e8f5ee',
      color: 'var(--status-success)',
      border: '1px solid #c4e6d3'
    },
    warning: {
      background: '#fef7e8',
      color: 'var(--status-warning)',
      border: '1px solid #f5e4b8'
    },
    error: {
      background: '#fce8e8',
      color: 'var(--status-error)',
      border: '1px solid #f0c4c4'
    }
  };
  const sizeStyles = {
    sm: {
      fontSize: '10px',
      padding: '2px 6px'
    },
    md: {
      fontSize: '11px',
      padding: '3px 10px'
    },
    lg: {
      fontSize: '13px',
      padding: '4px 12px'
    }
  };
  const style = {
    display: 'inline-flex',
    alignItems: 'center',
    fontFamily: 'var(--font-body)',
    fontWeight: 'var(--weight-semibold)',
    letterSpacing: 'var(--tracking-wide)',
    textTransform: 'uppercase',
    borderRadius: 'var(--radius-full)',
    lineHeight: '1.4',
    whiteSpace: 'nowrap',
    ...variantStyles[variant],
    ...sizeStyles[size]
  };
  return React.createElement('span', {
    style,
    ...rest
  }, children);
}
Object.assign(__ds_scope, { Badge });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Badge.jsx", error: String((e && e.message) || e) }); }

// components/core/Button.jsx
try { (() => {
function Button(props) {
  const {
    children,
    variant = 'primary',
    size = 'md',
    disabled = false,
    fullWidth = false,
    onClick,
    type = 'button',
    icon,
    iconPosition = 'left',
    ...rest
  } = props;
  const sizeStyles = {
    sm: {
      fontSize: 'var(--text-xs)',
      padding: '6px 14px',
      gap: '4px'
    },
    md: {
      fontSize: 'var(--text-sm)',
      padding: '10px 20px',
      gap: '6px'
    },
    lg: {
      fontSize: 'var(--text-base)',
      padding: '14px 28px',
      gap: '8px'
    }
  };
  const variantStyles = {
    primary: {
      background: 'var(--interactive-primary)',
      color: 'var(--text-on-gold)',
      border: '1px solid transparent',
      boxShadow: 'var(--shadow-gold)'
    },
    secondary: {
      background: 'var(--interactive-secondary)',
      color: 'var(--text-inverse)',
      border: '1px solid transparent',
      boxShadow: 'var(--shadow-sm)'
    },
    outline: {
      background: 'transparent',
      color: 'var(--gold-500)',
      border: '1px solid var(--border-gold)',
      boxShadow: 'none'
    },
    ghost: {
      background: 'transparent',
      color: 'var(--text-primary)',
      border: '1px solid transparent',
      boxShadow: 'none'
    }
  };
  const baseStyle = {
    display: 'inline-flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontFamily: 'var(--font-body)',
    fontWeight: 'var(--weight-semibold)',
    letterSpacing: 'var(--tracking-wide)',
    textTransform: 'uppercase',
    borderRadius: 'var(--radius-md)',
    cursor: disabled ? 'not-allowed' : 'pointer',
    opacity: disabled ? 0.5 : 1,
    transition: `background var(--duration-normal) var(--ease-default), box-shadow var(--duration-normal) var(--ease-default), border-color var(--duration-normal) var(--ease-default)`,
    textDecoration: 'none',
    lineHeight: '1',
    width: fullWidth ? '100%' : 'auto',
    ...variantStyles[variant],
    ...sizeStyles[size]
  };
  const [hovered, setHovered] = React.useState(false);
  const [pressed, setPressed] = React.useState(false);
  const hoverMap = {
    primary: {
      background: 'var(--interactive-primary-hover)'
    },
    secondary: {
      background: 'var(--interactive-secondary-hover)'
    },
    outline: {
      background: 'var(--gold-50)'
    },
    ghost: {
      background: 'var(--neutral-100)'
    }
  };
  const pressMap = {
    primary: {
      background: 'var(--interactive-primary-press)'
    },
    secondary: {
      background: 'var(--interactive-secondary-press)'
    },
    outline: {
      background: 'var(--gold-100)'
    },
    ghost: {
      background: 'var(--neutral-200)'
    }
  };
  const dynamicStyle = {
    ...baseStyle,
    ...(hovered && !disabled ? hoverMap[variant] : {}),
    ...(pressed && !disabled ? pressMap[variant] : {})
  };
  return React.createElement('button', {
    type,
    disabled,
    style: dynamicStyle,
    onClick,
    onMouseEnter: () => setHovered(true),
    onMouseLeave: () => {
      setHovered(false);
      setPressed(false);
    },
    onMouseDown: () => setPressed(true),
    onMouseUp: () => setPressed(false),
    ...rest
  }, icon && iconPosition === 'left' ? icon : null, children, icon && iconPosition === 'right' ? icon : null);
}
Object.assign(__ds_scope, { Button });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Button.jsx", error: String((e && e.message) || e) }); }

// components/core/Card.jsx
try { (() => {
function Card(props) {
  const {
    children,
    variant = 'default',
    padding = 'md',
    onClick,
    href,
    ...rest
  } = props;
  const paddingMap = {
    none: '0',
    sm: 'var(--space-3)',
    md: 'var(--space-6)',
    lg: 'var(--space-8)'
  };
  const variantStyles = {
    default: {
      background: 'var(--surface-primary)',
      border: '1px solid var(--border-default)',
      boxShadow: 'var(--shadow-md)'
    },
    elevated: {
      background: 'var(--surface-primary)',
      border: '1px solid var(--border-subtle)',
      boxShadow: 'var(--shadow-lg)'
    },
    outlined: {
      background: 'var(--surface-primary)',
      border: '1px solid var(--border-strong)',
      boxShadow: 'none'
    },
    gold: {
      background: 'var(--surface-gold)',
      border: '1px solid var(--border-gold-muted)',
      boxShadow: 'var(--shadow-gold)'
    },
    dark: {
      background: 'var(--surface-dark)',
      border: '1px solid var(--navy-500)',
      boxShadow: 'var(--shadow-lg)',
      color: 'var(--text-on-dark)'
    }
  };
  const [hovered, setHovered] = React.useState(false);
  const isInteractive = onClick || href;
  const style = {
    borderRadius: 'var(--radius-lg)',
    padding: paddingMap[padding],
    transition: `box-shadow var(--duration-normal) var(--ease-default), transform var(--duration-normal) var(--ease-default)`,
    cursor: isInteractive ? 'pointer' : 'default',
    textDecoration: 'none',
    display: 'block',
    color: 'inherit',
    ...variantStyles[variant],
    ...(hovered && isInteractive ? {
      boxShadow: 'var(--shadow-lg)',
      transform: 'translateY(-1px)'
    } : {})
  };
  const tag = href ? 'a' : 'div';
  const extraProps = href ? {
    href
  } : {};
  return React.createElement(tag, {
    style,
    onClick,
    onMouseEnter: () => setHovered(true),
    onMouseLeave: () => setHovered(false),
    ...extraProps,
    ...rest
  }, children);
}
Object.assign(__ds_scope, { Card });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Card.jsx", error: String((e && e.message) || e) }); }

// components/core/Divider.jsx
try { (() => {
function Divider(props) {
  const {
    variant = 'default',
    spacing = 'md',
    label,
    ...rest
  } = props;
  const spacingMap = {
    none: '0',
    sm: 'var(--space-3)',
    md: 'var(--space-6)',
    lg: 'var(--space-10)'
  };
  const variantStyles = {
    default: {
      borderColor: 'var(--border-default)'
    },
    gold: {
      borderColor: 'var(--gold-300)'
    },
    subtle: {
      borderColor: 'var(--border-subtle)'
    }
  };
  if (label) {
    const containerStyle = {
      display: 'flex',
      alignItems: 'center',
      gap: 'var(--space-4)',
      margin: `${spacingMap[spacing]} 0`
    };
    const lineStyle = {
      flex: 1,
      height: 0,
      borderTop: `1px solid ${variant === 'gold' ? 'var(--gold-300)' : 'var(--border-default)'}`
    };
    const labelStyle = {
      fontFamily: 'var(--font-body)',
      fontSize: 'var(--text-xs)',
      fontWeight: 'var(--weight-semibold)',
      letterSpacing: 'var(--tracking-widest)',
      textTransform: 'uppercase',
      color: variant === 'gold' ? 'var(--gold-500)' : 'var(--text-tertiary)',
      whiteSpace: 'nowrap'
    };
    return React.createElement('div', {
      style: containerStyle,
      ...rest
    }, React.createElement('div', {
      style: lineStyle
    }), React.createElement('span', {
      style: labelStyle
    }, label), React.createElement('div', {
      style: lineStyle
    }));
  }
  const hrStyle = {
    border: 'none',
    borderTop: '1px solid',
    margin: `${spacingMap[spacing]} 0`,
    ...variantStyles[variant]
  };
  return React.createElement('hr', {
    style: hrStyle,
    ...rest
  });
}
Object.assign(__ds_scope, { Divider });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Divider.jsx", error: String((e && e.message) || e) }); }

// components/core/Input.jsx
try { (() => {
function Input(props) {
  const {
    label,
    placeholder,
    value,
    onChange,
    type = 'text',
    size = 'md',
    error,
    helperText,
    disabled = false,
    required = false,
    id,
    ...rest
  } = props;
  const inputId = id || (label ? label.toLowerCase().replace(/\s+/g, '-') : undefined);
  const sizeStyles = {
    sm: {
      fontSize: 'var(--text-sm)',
      padding: '6px 10px'
    },
    md: {
      fontSize: 'var(--text-base)',
      padding: '10px 14px'
    },
    lg: {
      fontSize: 'var(--text-lg)',
      padding: '14px 16px'
    }
  };
  const [focused, setFocused] = React.useState(false);
  const containerStyle = {
    display: 'flex',
    flexDirection: 'column',
    gap: '4px',
    fontFamily: 'var(--font-body)',
    opacity: disabled ? 0.5 : 1
  };
  const labelStyle = {
    fontSize: 'var(--text-sm)',
    fontWeight: 'var(--weight-medium)',
    color: 'var(--text-primary)',
    letterSpacing: 'var(--tracking-normal)'
  };
  const inputStyle = {
    fontFamily: 'var(--font-body)',
    color: 'var(--text-primary)',
    background: 'var(--surface-primary)',
    border: error ? '1px solid var(--status-error)' : focused ? '1px solid var(--gold-400)' : '1px solid var(--border-default)',
    borderRadius: 'var(--radius-md)',
    outline: 'none',
    transition: `border-color var(--duration-normal) var(--ease-default), box-shadow var(--duration-normal) var(--ease-default)`,
    boxShadow: focused ? '0 0 0 2px var(--gold-200)' : 'none',
    lineHeight: 'var(--leading-normal)',
    width: '100%',
    boxSizing: 'border-box',
    ...sizeStyles[size]
  };
  const helperStyle = {
    fontSize: 'var(--text-xs)',
    color: error ? 'var(--status-error)' : 'var(--text-tertiary)',
    marginTop: '2px'
  };
  return React.createElement('div', {
    style: containerStyle
  }, label && React.createElement('label', {
    htmlFor: inputId,
    style: labelStyle
  }, label, required && React.createElement('span', {
    style: {
      color: 'var(--status-error)',
      marginLeft: '2px'
    }
  }, '*')), React.createElement('input', {
    id: inputId,
    type,
    placeholder,
    value,
    onChange,
    disabled,
    required,
    style: inputStyle,
    onFocus: () => setFocused(true),
    onBlur: () => setFocused(false),
    ...rest
  }), (helperText || error) && React.createElement('span', {
    style: helperStyle
  }, error || helperText));
}
Object.assign(__ds_scope, { Input });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Input.jsx", error: String((e && e.message) || e) }); }

__ds_ns.Avatar = __ds_scope.Avatar;

__ds_ns.Badge = __ds_scope.Badge;

__ds_ns.Button = __ds_scope.Button;

__ds_ns.Card = __ds_scope.Card;

__ds_ns.Divider = __ds_scope.Divider;

__ds_ns.Input = __ds_scope.Input;

})();
